#!/bin/env python3
# -*- coding:utf-8 -*-

# def p(date):
#     print(date)

def create_array():
    from numpy import arange, uint16, array

    a = arange(5)
    print("a = ",a," a.dtype = ",a.dtype," a.shape  = ",a.shape)

    m = array([arange(5),arange(10)])
    print("m = ",m," m.dtype = ",m.dtype," m.shape  = ",m.shape)

    t = arange(7, dtype = uint16)
    print("t = ",t," t.dtype = ",t.dtype)

def array_property():
    from numpy import arange
    
    a = arange(27).reshape(3,3,3)
    print("a = ", a)
    print("a.ndim = ",a.ndim)
    print("a.size = ",a.size)
    a.resize(3,9)
    # print("a.resize = ", a.resize(3,9))
    print("a = ", a)
    print("a.T = ", a.T)
    # p("a.T = ", a.T)

def lissajout():
    import sys
    from matplotlib.pyplot import plot,show
    from numpy import linspace,pi,sin
    
    a = float(sys.argv[1] )
    b = float(sys.argv[2] )
    
    t = linspace(-pi, pi, 201)
    x = sin(a + t + pi / 2)
    y = sin(b * t)
    plot(x,y)
    show()

def fourier():
    from numpy.fft import fft, ifft
    from matplotlib.pyplot import plot, show
    from numpy import linspace, pi, cos, abs, all

    x = linspace(0, 2 * pi, 30)
    wave = cos(x)
    transformed = fft(wave)
    print(all(abs(ifft(transformed) -wave) < 10 ** -9))
    plot(transformed)
    show()

    
def fourier2():
    from numpy.fft import fft, ifft
    from matplotlib.pyplot import plot, show
    import numpy as np

    x = np.linspace(0, 2 * np.pi, 30)
    wave = np.cos(x)
    transformed = fft(wave)
    print(np.all(np.abs(ifft(transformed) -wave) < 10 ** -9))
    plot(transformed)
    show()

def plot_sinc():
    from numpy import sinc, linspace
    from matplotlib.pyplot import plot, show

    x = linspace(0, 4, 100)
    vals = sinc(x)

    plot(x, vals)
    show()

def plot_sinc2d():
    from numpy import linspace, outer, sinc
    from matplotlib.pyplot import imshow, show

    x = linspace(0, 4, 100)
    xx = outer(x,x)
    vals = sinc(xx)

    print("x = ", x, " xx = ", xx, "vals = ", vals)
    imshow(vals)
    show()

def kaiser():
    from numpy import kaiser
    from matplotlib.pyplot import plot, show

    window = kaiser(42,14)
    plot(window)
    show()
    
if __name__ == '__main__':
    # create_array()
    # array_property()
    # lissajout()
    # print(sin(4))  # undefined
    # fourier()
    # fourier2()
    # plot_sinc()
    # plot_sinc2d()
    kaiser()
