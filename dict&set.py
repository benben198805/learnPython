print('-----------dict-------------')
score = {
    'A':95,
    'B':90,
    'C':80,
    'D':60,
}

print('A min limit is',score['A'])

print('use \'in\' to judge existtion')
if 'D' in score:
    print('D is exsit, and D is',score['D'])

print('\nor use \'get\' method to judge existtion')
print('D is',score.get('D'))

print('\nafter pop \'D\' key-value pair')
score.pop('D')
print(score)

print('-----------set-------------')
s = set([1,2,3,4])
print(s)
s.add(1)
print('after add 1, set is ',s)
s.add(5)
print('after add 5, set is ',s)
s.remove(5)
print('after remove 5, set is ',s)

print('-----------set is useful-------------')

a = set([1,2,3])
b = set([2,3,4])
print('a is', a)
print('b is', b)

print('a & b is', a&b)
print('a | b is', a|b)
