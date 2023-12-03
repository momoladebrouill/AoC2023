from pprint import pprint
f = open("input.txt", "r")

t = []

for line in f:
    t.append([e for e in line.strip()])

def isdigit(c):
    return '0' <= c <= '9'

nums = []
y = 0
for line in t:
    i = 0
    startpos = 0
    endpos = 0
    while i < len(line):
        if isdigit(line[i]):
            startpos = i
            while i<len(line) and isdigit(line[i]):
                i+=1
            nums.append(((startpos,y),i-1))
        else:
            i+=1
    y+=1

def get(x,y):
    if x < 0 or x >= len(t) : 
        return '.'
    if y < 0 or y >= len(t[0]) : 
        return '.'
    else:
        return t[y][x]

def around(startpos,endpos):
    sx,y = startpos
    l = []
    for x in range(sx-1,endpos+2):
        l.append((x,y+1))
        l.append((x,y-1))
    l.append((sx-1,y))
    l.append((endpos+1,y))
    return l

s = 0
def numify(startpos,endpos):
    return int(''.join(t[startpos[1]][startpos[0]:endpos+1]))

'''
for startpos,endpos in nums:
    if any([c != '.' for c in around(startpos,endpos)]): 
        v = ''.join(t[startpos[1]][startpos[0]:endpos+1])
        s+=int(v)
    else:
        v = ''.join(t[startpos[1]][startpos[0]:endpos+1])
        print(v)
'''

for y in range(len(t)):
    for x in range(len(t[y])):
        if get(x,y)=='*':
            adj = []
            adj += [numify(sp,ep) for sp,ep in nums if sp[1] == y-1 and sp[0]-1 <= x <= ep+1]
            adj += [numify(sp,ep) for sp,ep in nums if sp[1] == y+1 and sp[0]-1 <= x <=ep+1]
            adj += [numify(sp,ep) for sp,ep in nums if sp[1] == y and (ep == x-1 or sp[0] == x+1)]
            print(adj)
            if len(adj)==2:
                s+=adj[0]*adj[1]


for e in t:
    print(e)
print(s)
