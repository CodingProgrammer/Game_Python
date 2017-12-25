def file_save(boy, girl, count):
    boy_file_name = 'boy' + str(count) + '.txt'
    girl_file_name = 'girl' + str(count) + '.txt'
    boy_file = open(boy_file_name, 'w')
    girl_file = open(girl_file_name, 'w')
    boy_file.writelines(boy)
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

def file_split(file_name):
    f = open(file_name)
    count = 1
    boy = []
    girl = []
    for each_line in f:
        if each_line[:3] != '---':
            name, lines = each_line.split(':')
            if name == 'Jason':
                boy.append(lines)
            if name == 'PeiPei':
                girl.append(lines)                
        else:
            file_save(boy, girl, count)
            boy = []
            girl = []
            count += 1
    file_save(boy, girl, count)
    f.close()
file_split('dialog.txt')