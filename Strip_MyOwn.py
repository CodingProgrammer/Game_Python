# -*- coding: utf-8 -*-
def trim(s):
    if s.isspace() or  not s:
        return ''
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    return s
    '''
    if s.isspace() or  not s:
        return ''
    start = 0
    end = len(s) - 1
    while s[start] == ' ' or s[end] == ' ':
        if s[start] == ' ':
            start += 1
        if s[end] == ' ':
            end -= 1
    return s[start : end + 1]
    '''
# 测试: 
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
