"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isPrime(num):
    for i in range (2,num):
        if num%i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes<1:
        raise ValueError
    else:
        list = []
        num = 2
        while len(list)<number_of_primes:
            if isPrime(num):
                list.append(num)
            num+=1
        return list
