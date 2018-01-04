'''
两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。
The gcd of two ints equals to the gcd between min(x, y) and mod(x, y)
Here, we even need not to judege the min(x, y), why?
'''
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

a = int(input('a:'))
b = int(input('b:'))
print(gcd(a, b))