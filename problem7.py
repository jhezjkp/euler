#!/usr/bin/env python
#encoding=utf-8


"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


import time


def is_prime_num(num):
    n = 2
    while n < num / 2:
        if num % n == 0:
            return False
        n += 1
    return True

start = time.time()
count = 0
n = 1
while count <= 10001:
    n += 1
    if is_prime_num(n):
        count += 1

print n
print time.time() - start
