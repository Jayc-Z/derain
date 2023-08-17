import time
import gc
import torch
import math
import albumentations as A
import numpy as np

from albumentations.pytorch import ToTensorV2
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from tqdm import tqdm
# from torchsummary import summary
# from torchmetrics import PeakSignalNoiseRatio
from skimage import color
from skimage.metrics import structural_similarity

from Utils import load_checkpoint
from Dataset import ABDataset
from Model import Generator

gc.collect()
torch.cuda.empty_cache()

dataset_name = "EyeQ"  # "EyeQ" "Mendeley"

path = "Results"
checkpoint = "Results/genb.pth.tar"
save_path = f"Results/Testing {dataset_name}"
TEST_DIR = f"datasets/{dataset_name}/test"


def masking(a, b):
    l_top = l_bottom = 0
    a = a[0]
    b = b[0]

    for i in range(a.shape[1]):
        if torch.sum(a[:, i, :]) != 0:
            break
        l_top += 1

    for i in range(a.shape[1]):
        if torch.sum(a[:, a.shape[1] - i - 1, :]) != 0:
            break
        l_bottom += 1

    b[:, :l_top, :] = 0
    b[:, b.shape[1] - l_bottom:, :] = 0

    return a, b


def PSNR_SSIM(orig_img, gen_img):
    gray_orig_img = color.rgb2gray(orig_img)
    gray_gen_img = color.rgb2gray(gen_img)

    mse = np.mean((gray_orig_img - gray_gen_img) ** 2)
    if mse == 0:
        psnr = 100
    else:
        max_pixel = 1.0
        psnr = 20 * math.log10(max_pixel / math.sqrt(mse))

    ssim = structural_similarity(gray_orig_img, gray_gen_img, multichannel=False, data_range=1.0)

    return round(psnr, 3), round(ssim, 3)

orig_img, gen_img = "real_0.png", "fake_0.png"
psnr, ssim = PSNR_SSIM(orig_img, gen_img)
print(psnr, ssim)

