'Turn a string to integer'
from functools import reduce
def str2int(s):
    def fn(x,y):
        return 10 * x + y
    return reduce(fn,map(int, s))

'The following codes are testing code'
s = '12345'
n = str2int(s)
print(n)
print(type(n))
'''
The methods of changing a string to an integer
1. 
import string
s = '555'
n = string.atoi(s)

2.
n = int(s)
'''