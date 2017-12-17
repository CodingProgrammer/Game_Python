def findstr(string, sub_string):
    l_string = len(string)
    l_sub = len(sub_string)
    n = 0
    for i in range(l_string - l_sub + 1):
        if string[i:i + l_sub] == sub_string:
            n += 1
    return n

source = input("source string:")
sub = input('input sub-string:')
print(findstr(source, sub))