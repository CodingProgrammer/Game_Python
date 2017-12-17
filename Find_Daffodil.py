'''
Destination:find the Daffodil number
example:153 = 1^3 + 5^3 + 3^3
'''
def find_Daffodil(x):
    temp = x
    sum = 0
    while x / 10 > 0:
        sum += (x % 10) ** 3
        x /= 10
    sum += x ** 3
    if sum == temp:
        return True

l = range(100,1000)
for i in l:
    if find_Daffodil(i):
        print(i)