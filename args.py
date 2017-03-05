def calc(*number):
    sum = 0
    for x in number:
        sum = sum + x
    return sum


print('sum of 1 to 5 is',calc(*range(5)))
print('sum of 1 to 100 is',calc(*range(100)))

print('-----------------')


def person(name, age ,**kw):
    print('name:',name,',age:',age,',other:',kw)

person('Boo',12)
person('Boo',12,mother='Poo')
person('Boo',12,**{'sex':'man'})

print('-----------------')
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',**{'name':'boo'})
f1(*[1,2,3,4])