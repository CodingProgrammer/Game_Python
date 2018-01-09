'''
classmethod: has a implicit parameter
super()
string.format()
'''

import datetime

class PersonTyprError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

class Person:
    _count = 0

    @classmethod
    def get_count(cls):
        return Person._count

    def __init__(self, name, sex, age, ident):
        if not isinstance(name, str):
            raise PermissionError(name)
        if sex not in ('Male', 'Female') :
            raise PermissionError(sex)
        self._name = name
        self._sex = sex
        self._age = age
        self._id = ident
        Person._count += 1

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_sex(self):
        return self._sex

    def get_age(self):
        return self._age
    
    # <
    #make it possible to sort()
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PermissionError(another)
        return self._age < another.get_age()


    def __str__(self):
        para = 'Name:' + self._name + '\n' + 'Sex:' + self._sex + '\n' + 'Age:' + str(self._age) + '\n' + 'ID:' + str(self._id)
        return para

class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, age, department):
        super().__init__(name, sex, age, Student._id_gen())
        self._department = department
        self._course = {}
    def set_course(self, course_name):
        self._course[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._course:
            raise PersonValueError('No This Course!')
        else:
            if score < 0 or score > 100:
                raise PersonValueError('Bad Score!')
            else:
                self._course[course_name] = score
    def __str__(self):
        #para = 'Name:' + self._name + '\n' + 'Sex:' + self._sex + '\n' + 'Age:' + str(self._age) + '\n' + 'Department:' + str(self._department) +'\n' + 'ID:' + str(self._id)
        return super().__str__()  + '\n' + 'Department:' + str(self._department) + '\n' + 'Course:' + str(self._course)

class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '0{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, age, department, salary):
        super().__init__(name, sex, age, Staff._id_gen())
        if salary < 0:
            raise PersonValueError('No such salary')
        self._department = department
        self._salary = salary
        self._position = 'TBD'
    def get_salary(self):
        return self._salary
    def set_salary(self, salary):
        self._salary = salary

    def set_position(self, position):
        self._position = position

    def __str__(self):
        return super().__str__() + '\n' + 'Department:' + str(self._department) + '\n' + 'Salary:' + str(self._salary)+ '\n' + 'Position:' + str(self._position)
s1 = Student('Jason','Male', 24, 'JiLiang')
t1 = Staff('Wang', 'Male', '33', 'JiCe', 10000)
t1.set_position('教授')
print(t1)