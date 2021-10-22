# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from torchvision import datasets
import os
from icecream import ic
from tqdm import tqdm

classes = ('apple', 'aquarium_fish', 'baby', 'bear', 'beaver',
           'bed', 'bee', 'beetle', 'bicycle', 'bottle',
           'bowl', 'boy', 'bridge', 'bus', 'butterfly',
           'camel', 'can', 'castle', 'caterpillar', 'cattle',
           'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach',
           'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 'dolphin',
           'elephant', 'flatfish', 'forest', 'fox', 'girl',
           'hamster', 'house', 'kangaroo', 'keyboard', 'lamp',
           'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster',
           'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse',
           'mushroom', 'oak_tree', 'orange', 'orchid', 'otter',
           'palm_tree', 'pear', 'pickup_truck', 'pine_tree',
           'plain', 'plate', 'poppy', 'porcupine', 'possum',
           'rabbit', 'raccoon', 'ray', 'road', 'rocket',
           'rose', 'sea', 'seal', 'shark', 'shrew',
           'skunk', 'skyscraper', 'snail', 'snake', 'spider',
           'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table',
           'tank', 'telephone', 'television', 'tiger', 'tractor',
           'train', 'trout', 'tulip', 'turtle', 'wardrobe',
           'whale', 'willow_tree', 'wolf', 'woman', 'worm')

train_data = datasets.CIFAR100(root="./data/", train=True, download=True)
test_data = datasets.CIFAR100(root="./data/", train=False, download=True)

ic(len(train_data), len(test_data))
ic(train_data[0])
ic(train_data[0][0])

# RESULT
# ic| len(train_data): 60000, len(test_data): 10000
# ic| train_data[0]: (<PIL.Image.Image image mode=L size=28x28 at 0x7F94EF6E6AF0>, 5)
# ic| train_data[0][0]: <PIL.Image.Image image mode=L size=28x28 at 0x7F94EF6E6AF0>


saveDirTrain = './DataImages-Train'
saveDirTest = './DataImages-Test'

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
