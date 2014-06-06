#!/usr/bin/env python
#encoding=utf-8


import time


def is_factor_of_array(n, array):
    for i in array:
        if n % i != 0:
            return False
    return True

start = time.time()
array = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

n = 1
while not is_factor_of_array(n, array):
    n += 1
print n
print time.time() - start
