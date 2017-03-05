def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type')
    if x > 0:
        return x
    elif x == 0:
        pass
    else:
        return -x