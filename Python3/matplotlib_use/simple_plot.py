import numpy as np
import matplotlib.pyplot as plt

def simple_plot():
    func = np.poly1d(np.array([1,2,3,4]).astype(float))
    x = np.linspace(-10,10,30)
    y = func(x)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def simple_plot2():
    func = np.poly1d(np.array([1,2,3,4]).astype(float))
    func1 = func.deriv(m = 1)
    x = np.linspace(-10,10,30)
    y = func(x)
    y1 = func1(x)
    plt.plot(x,y,'ro',x,y1,'g--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def simple_subplot():
    func = np.poly1d(np.array([1,2,3,4]).astype(float))
    x = np.linspace(-10,10,30)
    y = func(x)

    func1 = func.deriv(m = 1)
    y1 = func1(x)

    func2 = func.deriv(m = 2)
    y2 = func2(x)

    plt.subplot(131)
    plt.plot(x,y,'r-')
    plt.title("Polynomial")

    plt.subplot(132)
    plt.plot(x,y1,'b^')
    plt.title("First Derivative")

    plt.subplot(133)
    plt.plot(x,y2,'go')
    plt.title("Second Derivative")
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def simple_plot_3d():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection = '3d')

    u = np.linspace(-1,1,100)
    x, y = np.meshgrid(u, u)
    z = x ** 2 + y ** 2
    ax.plot_surface(x, y, z, rstride = 4, cstride = 4, cmap = cm.YlGnBu_r)

    plt.show()

def simple_plot0():
    plt.figure()
    plt.show()

if __name__ == '__main__':
    #    simple_plot()
    # simple_plot2()
    # simple_subplot()
    # simple_plot_3d()
    simple_plot0()
