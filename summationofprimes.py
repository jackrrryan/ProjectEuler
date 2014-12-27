__author__ = 'kestrel'

import math

'''NOT DONE'''

def isprime(n):
    if n > 1:
        for i in range(2, int(n/2)):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return True

list = []

for i in range(1, 2000000):
    if isprime(i):
        print i
        list.append(i)

print list[:6]
print sum(list)
