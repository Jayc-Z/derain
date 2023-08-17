# -*- coding: utf-8 -*-
# @Time    : 2023/2/13 15:48
# @Author  : Curry
# @File    : multiscale.py

import torch
import torch.nn as nn

class Downscale2(nn.Module):
    def __init__(self, in_channels):
        super(Downscale2, self).__init__()
        self.in_channels = in_channels
        self.conv = nn.Sequential(
            nn.Conv2d(self.in_channels, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.max_pooling = nn.MaxPool2d(kernel_size=2,stride=2)

    def forward(self, x):
        x = self.conv(x)
        return self.max_pooling(x)

class Downscale4(nn.Module):
    def __init__(self, in_channels):
        super(Downscale4, self).__init__()
        self.in_channels = in_channels
        self.conv1 = nn.Sequential(
            nn.Conv2d(self.in_channels, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.max_pooling1 = nn.MaxPool2d(kernel_size=2, stride=2)

        self.conv2_1 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.conv2_2 = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        self.max_pooling2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.down4 = nn.Sequential(
            self.conv1,
            self.max_pooling1,
            self.conv2_1,
            self.conv2_2,
            self.max_pooling2,
        )

    def forward(self, x):
        return self.down4(x)

if __name__ == "__main__":
    x = torch.randn((5, 3, 256, 256))
    downscale_2 = Downscale2(in_channels=3)
    downscale_4 = Downscale4(in_channels=3)
    x_down2 = downscale_2(x)
    x_down4 = downscale_4(x)
    print(x_down2.shape)
    print(x_down4.shape)