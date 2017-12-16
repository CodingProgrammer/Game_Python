a = int(input("Input a number:"))
s = ''
while a >= 0:
    remainder = a % 2
    s += str(remainder)
    a = int(a / 2)
    if a == 0:
        break
s = s[::-1]
print('0b' + str(s))