#!/usr/bin/env python
# coding:utf-8
# Filename: turn_upper_suffix.py

import os


def main(path):
    i = 0
    
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path,name)):
            if name.split('.')[-1] == 'PNG':
                print(name)
                os.rename(os.path.join(path,name),os.path.join(path,name.split('.')[-2] + '.png'))
                i = i + 1

    return i 



if __name__ == '__main__':
    """ turn file suffix to upper case"""
    
    path_ = './'
    num = main(path_)
    print('conver ' + str(num) + ' files!')
