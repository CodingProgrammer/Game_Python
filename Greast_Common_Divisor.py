a = int(input("Input a:"))
b = int(input("Input b:"))
while b > 0:
    t = a % b
    a = b
    b = t
print("The Greast common divisor:" ,a)