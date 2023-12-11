from pprint import pprint
from math import sqrt
f = open("input.txt","r")
t = [[ e for e in line.strip()] for line in f.readlines()]

w = len(t[0])
h = len(t)
emptylines = [j for j in range(h) if all(t[j][i] == '.' for i in range(w))]
emptycols = [i for i in range(w) if all(t[j][i] == '.' for j in range(h))]

def prr(t):
    for j in t:
        for y in j:
            print(y,end="")
        print()

posgalaxies = []
for j,y in enumerate(t):
    for i,x in enumerate(y):
        if x == "#" :
            posgalaxies.append((i,j))

print(posgalaxies)
print(emptylines,emptycols)

def sgn(a,b):
    if a == b : return 1
    if b < a :
        return -1
    if b > a:
        return 1

def dist(a,b):
    dx = abs(a[0]-b[0]) + \
        (1000000-1) * len([col for col in emptycols if col in range(a[0],b[0],sgn(a[0],b[0]))]) 
    dy = abs(a[1]-b[1]) + \
        (1000000-1) * len([lin for lin in emptylines if lin in range(a[1],b[1],sgn(a[1],b[1]))]) 
    return dx+dy

distes = []
# produit cartésien de posgalaxies sur lui meme :
for x in posgalaxies:
    for y in posgalaxies:
        if x!=y:
            distes.append(dist(x,y))

print(int(sum(distes)/2))

    
