'the function just like title'
def normalize1(name):
    s = ' '.join(name) #list2str
    s = s.title()
    return s.split()   #str2list

def normalize2(name):
    return name.capitalize()

def normalize3(name):
    return name[0].upper() + name[1:].lower()

#the following codes are testing code
l = ['adam', 'LISA', 'barT']
print(normalize1(l))
print(map(normalize2, l))
print(map(normalize3, l))
