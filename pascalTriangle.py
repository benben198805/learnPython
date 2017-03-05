print('--------exercise-----------')
# import pdb
def pascalTriangle():
    l = [1]

    while True :
        list1 = l[:]
        list1.append(0)
        list2 =l[:]
        list2.insert(0, 0)
        l =  [sum(x) for x in zip(list1, list2)]
        yield l

n=0
for t in pascalTriangle():
    print(t)
    n = n+1
    if n==10:
        break