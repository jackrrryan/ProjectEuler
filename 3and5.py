__author__ = 'kestrel'

def find3or5():
    list = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
    print list
    print sum(list)

find3or5()
