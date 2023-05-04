#!/usr/bin/python3

import math


def minOperations(n):
    if n < 1:
        return 0

    # calculate the prime factors of n
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    # calculate the sum of the prime factors
    return sum(factors)
