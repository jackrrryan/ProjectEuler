__author__ = 'kestrel'

import math

count = 0
num = 0

def isprime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

list = []

while count != 10001:
    #print '{} {}'.format(count, num)
    if isprime(num):
        list.append(num)
        count += 1
    num += 1

print list
print len(list)
print list[10000]