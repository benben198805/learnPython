import math
def quadratic(a, b, c):
    mid = math.sqrt((b*b-4*a*c)/(4*a*a))
    firstResolve = (b*mid)/(2*a)
    secondResolve = -(b*mid)/(2*a)
    return firstResolve, secondResolve
