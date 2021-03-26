# 单例模式
class Singleton_one(object):

    obj = None
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.obj

# 单例模式
class Singleton_two(object):
    _singleton = {}

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = object.__new__(cls)
            return cls._singleton
        else:
            return cls._singleton


class Singleton_three(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton_three, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton_three):
    print(1)

class Singleton_four(object):
    _singleton = {}
    def __new__(cls, *args, **kwargs):
        origin = super(Singleton_four, cls).__new__()
        origin.__dict__ = cls._singleton
        return origin




my = MyClass()
print(id(my))
# 正则表达式
import re

p = re.compile('(blue|green|red)')
a = p.subn('color', 'green nlue blue red ')
b = p.subn('color', 'green nlue blue red', count=1)
print(a)
print(b)

a_list = []
b = (1, 3, 4)
c = {1: 2}
a_list.extend(b)
a_list.extend(c)
print(a_list)



class A():

    def foo(self):
        print('A foo')

class B(A):
    def foo(self):
        print('B foo')
        # A.foo(self)
        super(B, self).foo()

class C(A):
    def foo(self):
        print('C foo')
        # A.foo(self)
        super(C, self).foo()


class D(B, C):
    def foo(self):
        print('D foo')
        # B.foo(self)
        # C.foo(self)
        super(D, self).foo()

d = D()
print(d.foo())


a = map(lambda x: x*x, [i for i in range(10)])
print(a)
for i in a:
    print(i)

def atoi(s):
    pass

if __name__ == '__main__':
    string = '123'
    atoi(string)

import datetime

class TimeTest(Exception):

    def __init__(self, exception_info):
        super().__init__()
        self.info = exception_info

    def __str__(self):
        return self.info


def timecheck(func):

    def wrapper(*args, **kwargs):
        pass


def make_avg():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return average

avg = make_avg()
# avg(10)
print(avg(10))
print(avg(20))


# 装饰器实现输出函数的运行时间
import time

def clock(func):

    def clocked(*args):
        start_time = time.perf_counter()
        result = func(*args)
        end_time = time.perf_counter() - start_time

        name = func.__name__
        args_str = ','.join(repr(arg) for arg in args)
        return result
    return clocked

@clock
def a(j):
    for i in range(j):
        return i

a(100)


import time

DEFALUT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock_1(fmt=DEFALUT_FMT):
    def decorate(func):
        def closed(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time()
            name = func.__name__
            args = ','.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return closed
    return decorate

if __name__ == '__main__':
    @clock_1
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)


a = [1,2,3]
b = a
a.append(4)
print(b)

print(repr(123))
print(type(repr(123)))
vector = ''

a = "{'info': '货后100%月结5日(次月)', 'name': '当月结'}"

b = repr(a)
print(a)
print(b)