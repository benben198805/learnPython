listVar = list(range(10))

print('listVar is', listVar)
print('listVar[0:3] is', listVar[0:3])
print('listVar[:3] is', listVar[:3])
print('listVar[-1:-2] is', listVar[-1:-2])
print('listVar[-2:-1] is', listVar[-2:-1])
print('listVar[:-2] is', listVar[:-2])
print('listVar[:10:2] is', listVar[:10:2])


print('----------iteration----------')

d = {
    'a':1,
    'b':2,
    'c':3,
}
for key in d:
    print(key)

for key,value in d.items():
    print(key,':',value)

for i, value in enumerate(listVar):
    print(i,':',value)

location = [(1,1),(2,2),(3,3)]
for x, y in location:
    print(x,':',y)

print('--------gen list-----------')
firstList = list(range(10))
print(firstList)

secondList = [x*x for x in range(1,11)]
print(secondList)

thirdList = [x*x for x in range(1,11) if x%2==0]
print(thirdList)

thirdList = [m+n for m in 'ABC' for n in 'XYZ']
print(thirdList)

import os
fourthList = [d for d in os.listdir('.')]
print(fourthList)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)

print('--------generator-----------')

g1 = (x*x for x in range(1,11))
for n in g1:
    print(n)


def fib(max):
    n,a, b = 0,0,1
    while n<max:
        print(b)
        a, b= b, a+b
        n = n+1
    return 'done'

fib(5)

print('-------------------')

def fib_generator(max):
    n,a, b = 0,0,1
    while n<max:
        yield b
        a, b= b, a+b
        n = n+1
    return 'done'

print(fib_generator(5))
for x in fib_generator(5):
    print(x)

    