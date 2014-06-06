#!/usr/bin/env python
#encoding=utf-8


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
