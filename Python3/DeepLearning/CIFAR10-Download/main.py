#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Combofish
# Filename: main.py

from torchvision import datasets, transforms
from icecream import ic
import os
from tqdm import tqdm


train_data = datasets.CIFAR10(root="./data/", train=True, download=True)
test_data = datasets.CIFAR10(root="./data/", train=False, download=True)

ic(len(train_data), len(test_data))
ic(train_data[0])
ic(train_data[0][0])

saveDirTrain = './DataImages-Train'
saveDirTest = './DataImages-Test'

classes = ('airplane', 'automobile', 'bird', 'cat', 'dear', 'dog', 'frog', 'horse', 'ship', 'truck')

if not os.path.exists(saveDirTrain):
    os.mkdir(saveDirTrain)
    for sub_dir in classes:
        sub_dirs = os.path.join(saveDirTrain, sub_dir)
        if not os.path.exists(sub_dirs):
            os.mkdir(sub_dirs)

if not os.path.exists(saveDirTest):
    os.mkdir(saveDirTest)
    for sub_dir in classes:
        sub_dirs = os.path.join(saveDirTest, sub_dir)
        if not os.path.exists(sub_dirs):
            os.mkdir(sub_dirs)


def save_img(data, save_path):
    for i in tqdm(range(len(data))):
        img, label = data[i]
        f = os.path.join(save_path, classes[label], str(i) + '.png')
        img.save(f)


save_img(train_data, saveDirTrain)
save_img(test_data, saveDirTest)

