from pprint import pprint
import os
f = open("input.txt", "r")

qqtyinline = []
i = 0
for line in f.readlines():
    line = line[line.index(":")+1:][:-1]
    winning, numbers = [[x for x in e.split(' ') if x!= ''] for e in line.split('|')]
    qqty = len([num for num in numbers if num in winning])
    qqtyinline.append(qqty)
    i+=1
n = i
wonqqty = [1 for x in range(n)]
for i in range(n):
    for j in range(qqtyinline[i]):
        wonqqty[1+j+i] += wonqqty[i]
print(wonqqty)
print(sum(wonqqty))

