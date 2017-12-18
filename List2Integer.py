'Turn a sequence to an integer'
from functools import reduce
def fn(x,y):
    return 10 * x + y

l = [1,3,5,7,9]
n = reduce(fn, l) #fn here must take two parameters
print(n)