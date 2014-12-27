__author__ = 'kestrel'

with open('/home/kestrel/PycharmProjects/ProjectEuler/largestproductingrid') as f:
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()])

def horizontal():
    large = 0
    temp = 0
    for i in range(0, len(array[0])):
        for j in range(0, len(array[0])-3):
            temp = array[i][j] * array[i][j+1] * array[i][j+2] * array[i][j+3]
            if temp > large:
                large = temp
    return large

def vertical():
    large = 0
    temp = 0
    for j in range(0, len(array[0])):
        for i in range (0, len(array[0])-3):
            temp = array[i][j] * array[i+1][j] * array[i+2][j] * array[i+3][j]
            if temp > large:
                large = temp
    return large

def diag():
    large = 0
    temp = 0

    for i in range(0, len(array[0])-3):
        for j in range(0, len(array[0])-3):
            print '{} {} {} {}'.format(array[i][j], array[i+1][j+1], array[i+2][j+2], array[i+3][j+3])
            temp = array[i][j] * array[i+1][j+1] * array[i+2][j+2] * array[i+3][j+3]
            if temp > large:
                large = temp

    print 'large: {}'.format(large)

    print '-------------------------------------'

    for i in range(0, len(array[0])-3):
        for j in range(3, len(array[0])):
            print '{} {} {} {}'.format(array[i][j], array[i+1][j-1], array[i+2][j-2], array[i+3][j-3])
            temp = array[i][j] * array[i+1][j-1] * array[i+2][j-2] * array[i+3][j-3]
            if temp > large:
                large = temp

    print 'large: {}'.format(large)

    return large

master = []

master.append(horizontal())
master.append(vertical())
master.append(diag())

print master
print max(master)