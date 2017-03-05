list = [1,2,3,4,5]

print(list)

print('length of list is',len(list))

print('the first one of list is',list[0])

print('the last one of list is',list[-1])

list.append(6)

print('after append 6, list is ',list)

list.insert(0, -1)

print('after insert -1 in 0th position, list is ',list)

list.pop()

print('after pop, list is ',list)

list.pop(0)

print('after pop 0th element, list is ',list)

print('-----------------')

list = ['ABC', True, 123, [1,2]]

print(list)

print('and length of list is', len(list))

print('the [3,1] element is',list[3][1])

print('-----------------')

print('tuple like list, but cannot modify after init')

tuple = (1,2,3,4)

print(tuple)

print('one element tuple must define as (1,)')

oneEleTuple = (1,)

print(oneEleTuple[0])

print('--------exercise---------')

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
