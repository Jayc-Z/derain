import os
import numpy as np
from PIL import Image
from torch.utils.data import Dataset


class ABDataset(Dataset):
    def __init__(self, root_a, root_b=None, transform=None):
        self.root_a = root_a
        self.root_b = root_b
        self.transform = transform

        # rain200L
        # self.a_images = sorted(map(lambda x: x[:-4].split("_"), os.listdir(root_a)), key=lambda x: int(x[1]))
        # self.a_images = [x[0]+"_"+x[1]+".png" for x in self.a_images]
        # self.b_images = sorted(map(lambda x: x[:-4].split("_"), os.listdir(root_b)), key=lambda x: int(x[1]))
        # self.b_images = [x[0]+"_"+x[1]+".png" for x in self.b_images]

        self.a_images = sorted(os.listdir(self.root_a))
        self.b_images = sorted(os.listdir(self.root_b))
        self.length_dataset = max(len(self.a_images), len(self.b_images))
        self.a_len = len(self.a_images)
        self.b_len = len(self.b_images)

    def __len__(self):
        return self.length_dataset

    def __getitem__(self, index):
        if self.root_b is not None:
            a_img = self.a_images[index % self.a_len]
            a_path = os.path.join(self.root_a, a_img)
            a_img = np.array(Image.open(a_path).convert("RGB"))

            b_img = self.b_images[index % self.b_len]
            b_path = os.path.join(self.root_b, b_img)
            b_img = np.array(Image.open(b_path).convert("RGB"))

            if self.transform:
                augmentations = self.transform(image0=a_img, image=b_img)
                a_img = augmentations["image0"]
                b_img = augmentations["image"]

            return a_img, b_img

        elif self.root_b is None:
            a_img = self.a_images[index % self.a_len]
            a_path = os.path.join(self.root_a, a_img)
            a_img = np.array(Image.open(a_path).convert("RGB"))

            if self.transform:
                augmentations = self.transform(image=a_img)
                a_img = augmentations["image"]

            return a_img

if __name__ == '__main__':
    from torch.utils.data import DataLoader
    import albumentations as A
    from albumentations.pytorch import ToTensorV2
    TEST_DIR = "datasets/Rain200L/test/"
    transforms = A.Compose(
        [
            A.Resize(width=256, height=256),
            A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
            ToTensorV2(),
        ],
        additional_targets = {"image0":"image"},
        is_check_shapes = False
    )
    val_dataset = ABDataset(
        root_a=TEST_DIR + "norain", root_b=TEST_DIR + "rain", transform=transforms
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=1,
        shuffle=False,
        pin_memory=True,
    )
    for i, (norain, rain) in enumerate(val_loader):
        norain = norain
        rain = rain