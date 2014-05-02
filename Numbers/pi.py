from math import pi

def returnpi(n):
    """ returns pi to the nth digit """
    return round(pi, n)
    
if __main__ == '__name__':
    print returnpi(1)
    print returnpi(2)
    print returnpi(3)