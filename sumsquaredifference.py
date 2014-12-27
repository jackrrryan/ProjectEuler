__author__ = 'kestrel'

sqsum = 0

for i in range (1, 101):
    sqsum += i**2
print sqsum

numsum = 0
for j in range (1, 101):
    numsum += j
numsum = numsum**2
print numsum

print numsum - sqsum
