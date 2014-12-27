__author__ = 'kestrel'

NUM = 2520

def check(n):
    for i in range (1, 21):
        if n % i != 0:
            return False
        else:
            continue
    return True

def iterate():
    n = 2520
    i = 2
    x = False

    while x == False:
        print n
        if check(n) == True:
            return n
        else:
            n = NUM * i
            i += 1

print iterate()