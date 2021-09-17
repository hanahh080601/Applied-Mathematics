import math

def genprimes(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False

    for i in range(0, len(primes)):
        if primes[i] == True:
            print(i, end=" ")

n = int(input())
genprimes(n)