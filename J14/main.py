from pprint import pprint
f = open("input.txt","r")

t = [[e for e in line.strip()] for line in f.readlines()]
# --> x
# |
# $
# y

def get(t,x,y):
    if x < 0 or y < 0 or x >= len(t[0]) or y >= len(t):
        return '#'
    return t[y][x]

def _set(t,x,y,val):
    t[y][x] = val
# modifier la direction et le parcour
def tobemovedto(t,x,y,_dir):
    match _dir :
        case "N":
            s = (0,-1)
        case "S":
            s = (0,1)
        case "W":
            s = (-1,0)
        case "E":
            s = (1,0)
        case _ :
            print("efdfg")
    while 0<=y and 0<=x and y<len(t) and x<len(t[0]) and get(t,x+s[0],y+s[1]) == '.':
        x += s[0]
        y += s[1]
    return x,y

def parcours(t,_dir):
    # dir = N S E W
    if _dir == "N" :
        for y in range(len(t)):
            for x in range(len(t[0])):
                yield x,y
    if _dir == "S" :
        for y in range(len(t)-1,-1,-1):
            for x in range(len(t[0])):
                yield x,y
    if _dir == "N" :
        for y in range(len(t)):
            for x in range(len(t[0])):
                yield x,y
    if _dir == "W" :
        for x in range(len(t[0])):
            for y in range(len(t)):
                yield x,y
    if _dir == "E" :
        for x in range(len(t[0])-1,-1,-1):
            for y in range(len(t)):
                yield x,y
def h(t):
    return hash(''.join([''.join(l) for l in t]))

d = {}
for i in range(90):
    if h(t) in d.keys():
        print(i,d[h(t)])
    d[h(t)] = i
    for _dri in "NWSE":
        for x,y in parcours(t,_dri): 
            if get(t,x,y) == 'O':
                _set(t,x,y,'.')
                nx,ny = tobemovedto(t,x,y,_dri)
                _set(t,nx,ny,'O')
s = 0
for num,line in enumerate(t):
    s+=(len(t) - num) * len([e for e in line if e == 'O'])
 
print(s)
