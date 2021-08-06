#!/usr/bin/env python
# author: combofish
# Filename: one-line-print.py

from time import sleep

if __name__ == '__main__':
    count = 0
    
    for i in range(10):
        count = count + 1
        print("\r当前进度: {:.2f} %".format(count*100/ 10),end="")   
        sleep(1)



