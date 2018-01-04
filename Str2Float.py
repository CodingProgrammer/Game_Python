'''
This procesure use map, reduce, lambda 
idea:
1. we get a string contains '.' inside it
2. convert the string to a int, regardless of the '.'
3. find the index of '.' in the original string
4. use the int we get from step 2 divide 10^n, n equals to len(s) - 1 - string.index('.')
'''
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(x):
    return DIGITS[x]

def str2float(s):
    new_s = reduce(lambda x, y: 10 * x + y, map(str2int, ''.join(s.split('.'))))
    return new_s / (10 ** (len(s) - 1 - s.index('.')))

s = '.123456'
print(str2float(s))