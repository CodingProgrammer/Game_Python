print('''
|---新建用户：N/n---|
|---登录帐号：E/e---|
|---退出程序：Q/q---|
|---新建用户：N/n---|
''')
def create():
    name = input('请输入用户名：')
    while name in name_secret:
        name = input('此用户名已存在，请重新输入：')
    secret = input('请输入密码：')
    name_secret[name] = secret 

def enter():
    name = input('请输入用户名：')
    while name not in name_secret:
        name = input('此用户名不存在，请重新输入：')
    secret = input('请输入密码：')
    if secret == name_secret[name]:
        print('Welcome!')
    else:
        print('密码错误！')
name_secret = {}
while True:
    command = input('请输入指令代码：')
    if command == 'N' or command == 'n':
        create()
        
    if command == 'E' or command == 'e':
        enter()

    if command == 'Q' or command == 'q':
        break

print(name_secret)