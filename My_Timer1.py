import time as t 
class MyTimer:
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.tempstr = '未打开定时器!'
        self.runtime_sec = 0
    def __str__(self):
        return self.tempstr
    __repr__ = __str__
    def start(self):
        #start time
        self.tempstr = '请调用stop()停止记时！'
        print('记时开始！')
        self.begin = t.localtime()
    def stop(self):
        if not self.begin:
            print('请先打开计时器！')
        else:
            #stop time
            print('记时结束！')
            self.end = t.localtime()
            self._runtime()
    def _runtime(self):
        self.runtime = []
        self.tempstr = '总共运行了'
        for index in range(6):
            self.runtime.append(self.end[index] - self.begin[index])
        self.runtime_sec = self.runtime[5] + self.runtime[4] * 60 + self.runtime[3] * 3600
        self.tempstr += str(self.runtime_sec) + '秒'
        print(self.tempstr)
    def __add__(self, other):
        tempstr = '共运行了：'
        return tempstr + str(self.runtime_sec + other.runtime_sec) + '秒'
        
t1 = MyTimer()
t2 = MyTimer()
t1.start()
tim = input('Just wait:')
t1.stop()
t2.start()
tim = input('Just wait:')
t2.stop()
print(t1 + t2)