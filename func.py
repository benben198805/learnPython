print('--------exercise--------')

n1 = 255
n2 = 1000
print('hex result of 255 is',hex(n1))
print('hex result of 1000 is',hex(n2))



print('--------import my_abs--------')
from my_abs import my_abs
print('1 of abs is',my_abs(1))
print('-1 of abs is',my_abs(-1))
print('0 of abs is',my_abs(0))
# print('\'a\' of abs is',my_abs('a'))


print('--------return multi value--------')
import math
def move(x, y, step, angle=0):
    nx = x +step* math.cos(angle)
    ny = y +step* math.cos(angle)
    return nx, ny


x, y = move(100,100,60,math.pi/6)
print(x, y)
r = move(100,100,60,math.pi/6)
print(r)
print('returning multi value is just return a tuple')



print('--------exercise--------')
from quadratic import quadratic
print(quadratic(1,3,-4))
print(quadratic(1,5,-150))