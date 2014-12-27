__author__ = 'kestrel'

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
i = 0
v = 0
while v <= 4000000:
    v = fib(i)
    print v
    if v % 2 == 0:
        list.append(v)
    i += 1

print list
print sum(list)