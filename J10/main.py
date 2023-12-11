from pprint import pprint
import sys
from colorsys import hsv_to_rgb
import pygame as pg
f = open("input.txt", "r")
_map = [[e for e in line.strip()] for line in f.readlines()]
w = len(_map[0])
h = len(_map)
sys.setrecursionlimit(h*w)
'''
.....
.F-7.
.|.|.
.L-J.
.....
'''

dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def get(x,y):
    if x < w and y < h:
        return _map[y][x]
    else:
        return '.'

def getdir_map(x,y,_dir):
    _x = x + _dir[1] 
    _y = y + _dir[0] 
    if _x < w and _y < h:
        return _map[_y][_x]
    else:
        return '.'

def getdir_dist(x,y,_dir):
    _x = x + _dir[1] 
    _y = y + _dir[0] 
    if _x < w and _y < h:
        return distances[_y][_x]
    else:
        return 69420

def notvalid(x,y):
    # De morgan
    return x >= w or y >= h or x < 0 or y < 0
# can go to, can accept from
def connected(c):
    match c:
        case 'F':
            return [(1,0),(0,1)]
        case '-':
            return [(0,-1),(0,1)]
        case '7':
            return [(0,-1),(1,0)]
        case '|':
            return [(-1,0),(1,0)]
        case 'L':
            return [(-1,0),(0,1)]
        case 'J':
            return [(0,-1),(-1,0)]
        case 'S':
            return dirs
        case _:
            return []

distances = [ [-1 if _map[j][i] != 'S' else 0 for i in range(w)] for j in range(h)]
for j in range(h):
    for i in range(w):
        if _map[j][i] == 'S':
            start = (i,j)

# parcour en largeur

def parcour(l,dist):
    todo = []
    for (x,y) in l:
        if notvalid(x,y):
            continue
        distances[y][x] = dist
        for _dir in connected(get(x,y)): # pour chacun des voisins
            # non parcour, dans les tuyeaux, acceptant
            if getdir_dist(x,y,_dir) == -1 and getdir_map(x,y,_dir) != '.' and \
                (0,0) in [(_dir[1]+d[1],_dir[0]+d[0]) for d in connected(getdir_map(x,y,_dir))]: # non parcouru
                todo.append((x+_dir[1],y+_dir[0]))
    if len(todo) > 0:
        parcour(todo,dist+1)


parcour([start for d in dirs if getdir_map(start[0],start[1],d)!='.'],0)
def opposed(c):
    match c:
        case 'F':
            return ['J']
        case '7':
            return []
        case 'J':
            return []
        case 'L':
            return ['7']
        case _:
            return []
def isin(x,y):
    l = []
    b = 0
    for k in range(x,w):
        if _map[y][k] in ['|','S','F','7','L','J']:
            l.append(_map[y][k])
    for i in range(len(l)-1):
        if l[i+1] not in opposed(l[i]):
            b+=1
    return b % 2 == 1

qqty = 0
for j in range(h):
    for i in range(w):
        if isin(i,j):
            qqty+=1
print(qqty)

'''
for y in _map:
    for x in y:
        print(f"{x:2}"," ",end = "")
    print()
for y in distances:
    for x in y:
        print(" ." if x == -1 else f"{x%254:2x}",'',end = "")
    print()
'''
_max = 0
for j in range(h):
    for i in range(w):
        if distances[j][i] > _max:
            _max = distances[j][i]

"""
pg.init()
W = 700
H = 700
f=pg.display.set_mode((W,H),pg.RESIZABLE)
mask=pg.Surface((W,H),0)
mask.set_alpha(0.9)

b=True
fps=pg.time.Clock()
while b:
    #fps.tick(60)
    pg.display.update()
    f.blit(mask,(0,0))
    for j in range(h):
        for i in range(w):
            pg.draw.rect(f,
                0 if distances[j][i] == -1 else hsv_to_rgb(distances[j][i]/_max,1,255),
                (i/w*W,j/h*H,W/w-1,H/h-1))
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                b=pg.quit()
            case pg.KEYUP:
                if event.key==pg.K_ESCAPE:
                    b= pg.quit()
            case pg.VIDEORESIZE:
                W,H = event.w,event.h
                mask=pg.Surface((W,H),0)
                mask.set_alpha(0.1)
"""
