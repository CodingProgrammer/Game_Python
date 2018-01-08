'''
1. _gcd is a method which is static, has no self parameter. And it is really awesome tu put _gcd() in __init__
, that avoid referecing _gcd in every needed func.
2. Private parameters need a _ in front of them
3. Because we make _num and _den private, so we need methods to return them 
'''

class Rational10:
    @staticmethod
    def _gcd(a, b):
        while b > 0:
            t = a % b
            a = b
            b = t
        return a

    def __init__(self, num, den = 1):
        if num > 0 and den < 0:
            num, den = -num, -den
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        g = Rational10._gcd(num, den)
        self._num = num // g
        self._den = den // g

    def num(self):
        return self._num    

    def den(self):
        return self._den
    
    def __add__(self, another):
        den = self._den * another.den()
        num = self._num * another.den() + self._den * another.num()
        return Rational10(num, den)

    def __sub__(self, another):
        den = self._den * another.den()
        num = self._num * another.den() - self._den * another.num()
        return Rational10(num, den)

    def __mul__(self, another):
        num = self._num * another.num()
        den = self._den * another.den()
        return Rational10(num, den)

    def __floordiv__(self, another):
        if another.den() == 0:
            raise ZeroDivisionError
        return self * Rational10(another.den(), another.num())
    
    # ==
    def __eq__(self, another):                 
        return self._num *another.den() == self._den * another.num()
    # !=
    def __ne__(self, another):
        return self._num *another.den() != self._den * another.num()    

    # <
    def __lt__(self, another):
        return self._num *another.den() < self._den * another.num() 

    # >
    def __gt__(self, another):
        return self._num *another.den() > self._den * another.num() 
    # <=
    def __le__(self, another):
        return self._num *another.den() <= self._den * another.num()

    # >=
    def __ge__(self, another):
        return self._num *another.den() >= self._den * another.num()

    def printit(self):
        if self._num == self._den:
            print('1')
        elif self._num == 0:
            print('0')
        elif self._num == -self._den:
            print('-1')
        else:
            print(str(self._num) + '/' + str(self._den))
    def __str__(self):
        if self._num == self._den:
            return '1'
        elif self._num == 0:
            return '0'
        elif self._num == -self._den:
            return '-1'
        return str(self._num) + '/' + str(self._den)


n1 = Rational10(1,-2)
n2 = Rational10(1,-3)
n3 = Rational10(1,2)
n1.printit()
n2.printit()
n3.printit()
print(n1 <= n3)
print(n1)