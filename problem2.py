#!/usr/bin/env python
#encoding=utf-8


first = 1
second = 2
sum = second
third = first + second
while third < 4000000:
    if third % 2 == 0:
        sum += third
    first, second = second, third
    third = first + second

print sum
