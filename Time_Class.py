class Time:
    def __init__(self, h = 0, m = 0, s = 0):
        if h > 24 or m > 60 or s > 60:
            raise ValueError(h, m, s)
        self._hour = h
        self._min = m
        self._sec = s
    def hours(self): return self._hour

    def minutes(self): return self._min

    def seconds(self): return self._sec

    def __add__(self, another):
        if not isinstance(another, Time):
            raise TypeError(another)
        temp = (self._hour + another.hours()) * 3600 + (self._min + another.minutes()) * 60 + (self._sec + another.seconds())
        h = temp // 3600
        m = (temp % 3600) // 60
        s = temp % 60
        return Time(h,m,s)

    def __sub__(self, another):
        if not isinstance(another, Time):
            raise TypeError(another)
        temp = (self._hour - another.hours()) * 3600 + (self._min - another.minutes()) * 60 + (self._sec - another.seconds())
        if temp < 0:
            raise ValueError('Bing is smaller than Meiosis')
        h = temp // 3600
        m = (temp % 3600) // 60
        s = temp % 60
        return Time(h,m,s)

    def __eq__(self, another):
        if not isinstance(another, Time):
            raise TypeError(another)
        return self._hour == another.hours() and self._min == another.minutes() and self._sec == another.seconds()

    def __lt__(self, another):
        if not isinstance(another, Time):
            raise TypeError(another)
        if self._hour < another.hours():
            return True
        elif self._hour == another.hours():
            if self._min < another.minutes():
                return True
            elif self._min == another.minutes():
                if self._sec < another.seconds():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __str__(self):
        return 'hour:{}  Minutes:{}  Seconds:{}'.format(self._hour, self._min, self._sec)

t1 = Time(8, 20, 20)
t2 = Time(8, 20)
print(t2 < t1)