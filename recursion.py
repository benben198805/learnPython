def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print('the Factorial of 1 is',fact(1))
print('the Factorial of 2 is',fact(2))
print('the Factorial of 3 is',fact(3))
print('the Factorial of 4 is',fact(4))


print('-----------------------------------')

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num -1, product * num)


print('the Factorial of 1 is',fact_iter(1,1))
print('the Factorial of 2 is',fact_iter(2,1))
print('the Factorial of 3 is',fact_iter(3,1))
print('the Factorial of 4 is',fact_iter(4,1))

print('-------------Tower of Hanoi---------------')

def Hanoi(n, a, b, c):
    if n <1:
        return
    Hanoi(n-1,a,c,b)
    print('move %dth plate from %s to %s'%(n, a, c))
    Hanoi(n-1,b,a,c)


Hanoi(1, 'A', 'B', 'C')
Hanoi(3, 'A', 'B', 'C')