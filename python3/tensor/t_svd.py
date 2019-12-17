#!/usr/bin/env python
# author: combofish
# Filename: t_svd.py

import numpy as np


def t_svd(X):
    """X as three dim"""

    N = X.ndim
    L = np.prod(X.shape[2:])
    
    X = np.fft.fft(X)
    # for i in range(X.shape[-1]):
    U1 = np.zeros([X.shape[0],X.shape[0],L])
    S1 = np.zeros([X.shape[0],X.shape[1],L])
    V1 = np.zeros([X.shape[1],X.shape[1],L])
        
    for i in range(L):
        # print(X[:,:,i])
        U,S,V = np.linalg.svd(X[:,:,i])
        U1[:,:,i],S1[:,:X.shape[0],i],V1[:,:,i] = U, np.diag(S),V

    # for i in range(2:N):
    U = np.fft.ifft(U1)
    S = np.fft.ifft(S1)
    V = np.fft.ifft(V1)

    return (U,S,V)


if __name__ == '__main__':
    X = np.arange(24).reshape(2,3,4)
    # t_svd(X)
    
    U,S,V = t_svd(X)
    # print(X)
    print(U,S,V)
    print(U.shape,S.shape,V.shape)
