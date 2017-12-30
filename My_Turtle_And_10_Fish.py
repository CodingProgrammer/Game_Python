'''
There is a problem of run out of range when pop
And do not know why yet!!!
#It is very dangerous to delete an element from iterator, cause the iterator reference the element to reference directly
And there is a bug that all the fishes and turtle unexpect to move ti the border finally, so that means there is a bug in the move section 
'''
import random
class Turtle:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        self.endurance = 100
        #self.step = random.randint(1, 2)
    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    def move(self):
        flag = random.randint(0, 1)
        step = random.choice([-2, -1, 1, 2])
        if flag == 0:                     #flag = 0 means move x
            new_x = self.x + step
            self.endurance -= 1
            if new_x > 10:
                self.x = 20 - new_x
            elif new_x < 0:
                self.x = 0 - new_x
            else:
                self.x = new_x
        else:                             #flag = 1 means move y   
            self.endurance -= 1                                                             
            new_y = self.y + step
            if new_y > 10:
                self.y = 20 - new_y
            elif new_y < 0:
                self.y = 0 - new_y
            else:
                self.y = new_y
        return str(self.x) + ',' +str(self.y)
    def get_Location(self):
        print('乌龟的位置：',self.x, self.y, sep = ' ')   

    def get_Endur(self):
        print('小龟龟所剩余的体力：', self.endurance) 

class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    def move(self):
        flag = random.randint(0, 1)
        step = random.choice([-1, 1])
        if flag == 0:                     #flag = 0 means move x
            new_x = self.x + step
            if new_x > 10:
                self.x = 20 - new_x
            elif new_x < 0:
                self.x = 0 - new_x
            else:
                self.x = new_x
        else:                            #flag = 1 means move y                                       
            new_y = self.y + step
            if new_y > 10:
                self.y = 20 - new_y
            elif new_y < 0:
                self.y = 0 - new_y
            else:
                self.y = new_y
        return str(self.x) + ',' +str(self.y)
    def get_Location(self):
        print('鱼的位置：', self.x, ', ' ,self.y,)
t1 = Turtle()
t1.get_Location()
f = []
for i in range(10):
    f.append(Fish())
    print(f[i])
while True:
    if t1.endurance == 0:
        print('The Turtle is dead!Game Over!')
        break
    if len(f) == 0:
        print('All the fishes are eaten! Game Over!')
        break
    t_pos = t1.move()
    t1.get_Endur()
    for each_fish in f[:]:              #It is very dangerous to delete an element from iterator
        if t_pos == each_fish.move():   #cause the iterator reference the element to reference directly
            t1.endurance += 20
            f.remove(each_fish)
            print('有一条鱼被吃掉了，呜呜呜呜～～～～～～')                   
        
        
    i -= 1
print('Run Out')