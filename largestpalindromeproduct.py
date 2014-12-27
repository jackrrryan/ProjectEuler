__author__ = 'kestrel'

list = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        p = str(i * j)
        rev_p = p[::-1]
        if p == rev_p:
            print p
            list.append(int(p))

print list
print max(list)