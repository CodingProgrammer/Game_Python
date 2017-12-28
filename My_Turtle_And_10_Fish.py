'''
There is a problem of run out of range when pop
And do not know why yet!!!
'''
import random
class Turtle:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.endurance = 100
        #self.step = random.randint(1, 2)
    def move(self):
        flag = random.randint(0, 1)
        step = random.randint(1, 2)
        if flag == 0:
            if step == 1:
                if self.x >= 10:
                    self.x -= 1
                    self.endurance -= 1
                else:
                    self.x += 1
                    self.endurance -= 1
            elif step == 2:
                if self.x >= 9:
                    self.x -= 2
                    self.endurance -= 1
                else:
                    self.x += 2
                    self.endurance -= 1
        else:
            if step == 1:
                if self.y >= 10:
                    self.y -= 1
                    self.endurance -= 1
                else:
                    self.y += 1
                    self.endurance -= 1
            elif step == 2:
                if self.y >= 9:
                    self.y -= 2
                    self.endurance -= 1
                else:
                    self.y += 2
                    self.endurance -= 1
    def get_Location(self):
        print('乌龟的位置：',self.x, self.y, sep = ' ')   

    def get_Endur(self):
        print('小龟龟所剩余的体力：', self.endurance) 

class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
    def move(self):
        flag = random.randint(0, 1)
        if flag == 0:
            if 0 <= self.x < 10:
                self.x += 1
            elif self.x >= 10:
                self.x -= 1
            else:
                self.x += 1
        else:
            if 0 <= self.y < 10:
                self.y += 1
            elif self.y >= 10:
                self.y -= 1
            else:
                self.y += 1
    def get_Location(self, index):
        print('鱼%d的位置：' %index, self.x, self.y, sep = ' ')
t1 = Turtle()
t1.get_Location()
f = []
for i in range(10):
    f.append(Fish())
    f[i].get_Location(i)
i = 40
while i > 0:
    index_todelete = []
    if t1.endurance == 0 or len(f) == 0:
        print('Game Over!')
        break
    t1.move()
    t1.get_Location()
    t1.get_Endur()
    for j in range(len(f)):
        f[j].move()
        f[j].get_Location(j)
        if t1.x == f[j].x and t1.y == f[j].y:
            t1.endurance += 20
            index_todelete.append(j)
    for index in index_todelete:
        f.pop(index)
        print('有一条鱼被吃掉了，呜呜呜呜～～～～～～')
    i -= 1
print('run out')