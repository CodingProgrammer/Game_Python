#!/bin/python3
import sys
n = int(input().strip())
n_binary = bin(n)[2:]
n_length = 0
l = []
for c in n_binary:
    if c == '1':
        n_length += 1
    else:
        l.append(n_length)
        n_length = 0
    l.append(n_length)
print(max(l))