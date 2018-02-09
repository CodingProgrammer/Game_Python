#!/bin/python3

import sys

def staircase(n):
    for i in range(1, n + 1):
       print('%*s'%(n, '#' * i))


n = 4
staircase(n)
