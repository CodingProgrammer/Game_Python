h = input('height(m): ')
height = float(h)
w = input('weight(kg): ')
weight = float(w)
bmi = float(weight / (height * height))
print(bmi)
if bmi < 18.5:
    print('����')
elif bmi >= 18.5 and bmi < 25:
    print('����')
elif bmi >= 25 and bmi < 28:
    print('����')
elif bmi >= 28 and bmi < 32:
    print('����')
else:
    print('���ط���')
    

