def parentheses(s):
    if '+' in s:
        a, b = map(int, s.split('+'))
        return a + b
    elif '-' in s:
        a, b = map(int, s.split('-'))
        return a - b
    elif '*' in s:
        a, b = map(int, s.split('*'))
        return a * b
    elif '/' in s:
        a, b = map(int, s.split('/'))
        return a / b

def concise(arr):
    length = len(arr)
    i = 0
    res = []
    while i < length:
        if arr[i].isdigit():
            temp = ''
            while i < length and arr[i].isdigit():
                temp += arr[i]
                i += 1
            res.append(int(temp))
        else:
            if '-' in arr[i] and len(arr[i]) > 1:
                res.append(-int(arr[i][1:]))
            else:
                res.append(arr[i])
            i += 1
    return res

def calculate(arr):
    # */
    i =  0
    temp = [] 
    while i < len(arr):
        if arr[i] == '*':
            temp.append(temp.pop() * arr[i+1])
            i += 1

        elif arr[i] == '/':
            temp.append(temp.pop() / arr[i+1])
            i += 1
        else:
            temp.append(arr[i])
        i += 1
    j = 0
    res = 0
    pre = 0
    while j < len(temp):
        if temp[j] == '+':
            res += (pre + temp[j+1])
            j += 1
        
        elif temp[j] == '-':
            res += (pre - temp[j+1])
            j += 1
        else:
            pre = temp[j]
        j += 1
    return res

def formulaToNum(s):
    myStack = []
    for each in s:
        if each == ')' and '(' in myStack:
            temp = []
            while myStack[-1] != '(':
                temp.append(myStack.pop())
            myStack.pop()
            myStack.append(str(parentheses(''.join(temp[::-1]))))
        else:
            myStack.append(each)
    myStack = concise(myStack)
    return (calculate(myStack))

s = '48*((70-65)-45)+8*1'
print(formulaToNum(s))
