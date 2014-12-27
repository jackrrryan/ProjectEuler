__author__ = 'kestrel'

import math

def pyt():
    for i in range(1, 1000):
        for j in range(1, 1000):
            sum = math.sqrt(i**2 + j**2)
            if sum.is_integer():
                print '{} {}'.format(i, j)
                if sum > i and sum > j:
                    if sum + i + j == 1000:
                        return sum * i * j

print pyt()