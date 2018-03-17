class Person(object):
    def __init__(self, name):
        self.name = name
        self.gun = None#用来保存枪对象的引用
        self.hp = 100
    def push_bullets(self, dan_jia_temp, bullet_temp):
        """把子弹装到弹夹中"""
        dan_jia_temp.zhuang_dan(bullet_temp)

    def anzhaung_danjia(self, gun_temp, dan_jia_temp):
        """把弹夹安装到枪中"""
        gun_temp.baocun_danjia(dan_jia_temp)
    def naqiang(self, gun_temp):
        """老王拿起一把枪"""
        self.gun = gun_temp
    
    def shoot(self, target):
        if target.hp > 0:
            #开枪射击
            self.gun.fire(target)
        else:
            print('敌人已死，请勿鞭尸！')
    def __str__(self):
        if self.gun:
            return "%s他有枪,血量为：%d,枪的信息为：%s"%(self.name, self.hp, self.gun)
        else:
            return "%s他没枪,血量为：%d"%(self.name, self.hp)

class Gun(object):
    def __init__(self, name):
        self.name = name
        self.danjia = None#用来记录弹夹对象的引用
    def baocun_danjia(self, dan_jia_temp):
        """用一个属性保存这个弹夹对象的引用"""
        self.danjia = dan_jia_temp
    def fire(self, target):
        bullet_temp = self.danjia.get_zidan()
        if bullet_temp:
            target.hp -= bullet_temp.get_shanghai()
        else:
            print("没子弹了！")
    def __str__(self):
        if self.danjia:
            return  "枪的类型为：%s, 弹夹信息为：%s" %(self.name, self.danjia)
        else:
            return "枪的类型为：%s, 这把枪中没有弹夹" %self.name
        
class Danjia(object):
    def __init__(self, num_max):
        self.num_max = num_max#子弹的个数
        self.bullet_list = []#用来记录所有子弹的引用
    def zhuang_dan(self, bullet_temp):
        """将这颗子弹保存"""
        if len(self.bullet_list) < self.num_max:
            self.bullet_list.append(bullet_temp)
    def get_zidan(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None
        
    def __str__(self):
        return "弹夹的信息：%d/%d"%(len(self.bullet_list), self.num_max)

class Bullets(object):
    def __init__(self, shanghai):
        self.shanghai = shanghai#子弹的威力
    def get_shanghai(self):
        return self.shanghai 
def main():
    #1 创建老王
    laowang = Person("老王")
    ak47 = Gun("AK47")
    dan_jia = Danjia(20)
    for i in range(15):
        bullet = Bullets(10)
        #老王把子弹安装到弹夹中
        laowang.push_bullets(dan_jia, bullet)
    #老王安装弹夹到枪中
    laowang.anzhaung_danjia(ak47, dan_jia)
    #老王拿枪
    laowang.naqiang(ak47)
    print(laowang)
    print(ak47)
    gebi_laomeng = Person("隔壁老孟")
    print(gebi_laomeng)
    for j in range(11):
        laowang.shoot(gebi_laomeng)
    print(gebi_laomeng)
    print(ak47)
if __name__ == '__main__':
    main()