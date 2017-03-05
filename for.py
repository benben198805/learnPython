print('--------for------------')
list = [1,2,3,4,5]

for item in list:
    print(item)

sum = 0
for item in list:
    sum += item
print('sum is',sum)

sumForOneToHundred = 0
for item in range(100):
    sumForOneToHundred+=item
print(sumForOneToHundred)

print('----exercise--exercise-----')
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello',x)

print('---------while-----------')
n = 1
while n<=5:
    print(n)
    n = n+1
print('end')

print('---------braak-----------')
n = 1
while n<=5:
    if n == 3:
        print('break at 3')
        break
    print(n)
    n = n+1
print('end')

print('---------continue-----------')
n = 1
while n<=5:
    n = n+1
    if n == 3:
        print('jump over 3')
        continue
    print(n)
print('end')