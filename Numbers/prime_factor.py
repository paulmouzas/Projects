def isFactor(n1, n2):
    """ determines if n1 is a factor of n2 """
    if n1 == 0 or n2 == 0: return None
    return n2 % n1 == 0
    
def isPrime(n):
    if n%2 == 0: return False
    for i in range(2, n):
        if n%i==0: return False
    return True

def primeFactors(n):
    return [x for x in range(2,n) if isPrime(x)==True and isFactor(x,n)==True]
    
print primeFactors(129)
    