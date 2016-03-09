from ctypes import *
import os

path = os.getcwd()
libc = CDLL(path + '/src/libmymath.so')

def add_float(a, b):
    
    libc.add_float.argtypes = [c_float, c_float]
    libc.add_float.restype = c_float

    return libc.add_float(a, b)


def add_int(a, b):
    
    libc.add_int.argtypes = [c_int, c_int]
    libc.add_int.restype = c_int

    return libc.add_int(a, b)


def add_float_ref(a, b, c):

    a = c_float(a)
    b = c_float(b)
    c = c_float(c)

    libc.add_float_ref(byref(a), byref(b), byref(c))
   
    return c.value


def dot_product(a, b):

    libc.dot_product.restype = c_float

    n = c_int(len(a))

    a = (c_float * n.value) (*a)
    b = (c_float * n.value) (*b)

    res = libc.dot_product(a, b, n)
    
    return res


def main():

    a = 2
    b = 3
    c = 0

    print add_float(a, b)

    print add_float_ref(a, b, c)

    a = [2, 3]
    b = [1, 2]

    print dot_product(a,b)
    


if __name__ == "__main__":
    main()


