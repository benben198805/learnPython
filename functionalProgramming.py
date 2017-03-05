print('---------map----------')
def f(x):
    return x*x

print(list(map(f, *[range(10)])))

print(list(map(str, *[range(10)])))

print('---------reduce----------')
from functools import reduce
def addItem(a, b):
    return a+b

print(reduce(addItem,[1,2,3,4,5]))

def char2num(a, b):
    return a*10+b

print(reduce(char2num,[1,2,3,4,5]))

print('---------exercise 1----------')
names = ['adam', 'LISA', 'barT']

def normalName(name):
    return name[0].upper()+name[1:].lower()

print(list(map(normalName, names)))

print('---------exercise 2----------')

def pro(x, y):
    return x*y

def prod(L):
    return reduce(pro, L)

print(prod([1,2,3,4,5,6,7,8,9]))

print('---------exercise 3----------')

import math
def str2float(s):
    def fn(x, y):
        if y == '.':
            return x
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':'.'}[s]
    size = len(s) - s.index('.')-1 if s.index('.')>-1 else 0
    return reduce(fn, map(char2num, s)) * (math.pow(0.1, size))

print(str2float('123.123'))


print('---------filter----------')
def is_odd(x):
    return x%2==1

print(list(filter(is_odd,*[range(10)])))

print('---------exercise 4----------')

def is_palindrome(x):
    rawStr = str(x)
    revertStr = rawStr[::-1]
    return rawStr == revertStr

output = filter(is_palindrome, range(1, 1000))
print(list(output))

print('---------sort----------')
print(sorted([-5,1,2,3,-4], key=abs))
print(sorted([-5,1,2,3,-4], key=abs, reverse=True))

print('---------exercise 5----------')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(x):
    return x[0]

L2 = sorted(L, key=by_name)
print(L2)




