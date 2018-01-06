print(
'''
|---欢迎进入通讯录程序---|
|---1:查询联系人资料---|
|---2：插入新的联系人---|
|---3：删除已有的联系人---|
|---4：退出通讯录程序---|
''')
phone_book = {}
while True:
    n = int(input('请输入相关的指令代码：'))

    if n == 4:
        break

    elif n == 1:
        name = input('请输入联系人姓名：')
        if name in phone_book:
            print(name + ':' + phone_book[name])
        else:
            print('用户不存在')
        continue

    elif n == 2:
        name = input('请输入联系人姓名：')

        if name in phone_book:
            print('您输入的姓名已存在-->> ' + name + ':' + phone_book[name])
            yes_or_no = input('是否修改用户资料(YES/No):')
            if yes_or_no == 'YES':
                new_number = input('请输入新的电话号码：')
                phone_book[name] = new_number
                
            else:
                print('不改就不改')
                
        else:
            number = input('请输入联系人电话:')  
            phone_book[name] = number  
        continue
    
    elif n == 3:
        name = input('请输入要删除联系人：')
        if name in phone_book:
            phone_book.pop(name)
            
        else:
            print('您要删除的联系人不存在！')
        continue    

    else:
        print('输入无效，请输入1～4之间的整数！')
        continue

print(phone_book)
print('感谢使用通讯录！')