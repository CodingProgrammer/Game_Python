def calculate(arr):
    temp_stack = []
    for each in arr:
        if temp_stack and temp_stack[-1] == '*':
            temp_stack.pop()
            temp_stack.append(temp_stack.pop() * each)
        elif temp_stack and temp_stack[-1] == '/':
            temp_stack.pop()
            temp_stack.append(temp_stack.pop() // each)
        else:
            temp_stack.append(each)

    res = []
    for i in range(len(temp_stack)):
        if res and res[-1] == '+':
            res.pop()
            res.append(res.pop() + temp_stack[i])
        elif res and res[-1] == '-':
            res.pop()
            res.append(res.pop() - temp_stack[i])
        else:
            res.append(temp_stack[i])
    return sum(res)

def formula(s, index):
    i = index
    myStack = []
    temp_num = 0
    while i < len(s) and s[i] != ')':
        if s[i] == '(':
            retrurn_data = formula(s, i+1)
            myStack.append(retrurn_data[0])
            i = retrurn_data[1]
        else:
            if s[i].isdigit():
                temp_num = temp_num * 10 + int(s[i])
            else:
                if s[i-1].isdigit():
                    myStack.append(temp_num)
                    temp_num = 0
                myStack.append(s[i])
            i += 1
    if s[i-1] != ')':
        myStack.append(temp_num)
    return (calculate(myStack), i + 1)

if __name__ != 'main':
    s = '2*(1+(24/(2+3*(4-2))))'
    print(formula(s, 0)[0])
