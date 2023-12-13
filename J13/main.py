from pprint import pprint
f = open("input.txt","r")

t =[]
l =[] 

for line in f.readlines():
    line = line.strip()
    if line == '':
        t.append(l)
        l=[]
    else:
        l.append([ e for e in line])
t.append(l)

def convert(a):
    s = 0
    puis = 1
    for e in a:
        s+= puis * (1 if e == '#' else 0)
        puis *= 2
    return s

def ismirrored(l,ind,s):
    # la valeur max de i
    i = 0
    while 0 <= ind - i  and ind + 1 + i < s:
        if l[ind-i] != l[ind+1+i]:
            return False
        i+=1
    return True
# l * 100 + c

def scorefroml(sc,sl):
    return sum(sc) + 100* sum(sl)
def getscore(part):
    w = len(part[0])
    h = len(part)
    lignes = [convert(e) for e in part]
    colones = [convert(part[i][j] for i in range(h)) for j in range(w)]
    sc = []
    for j in range(len(colones)-1):
        if ismirrored(colones,j,len(colones)):
            sc.append(j+1)
    sl = []
    for i in range(len(lignes)-1):
        if ismirrored(lignes,i,len(lignes)):
            sl.append(i+1)
    return sc,sl

def swap(c):
    if c == "#":
        return '.'
    if c == '.':
        return '#'
    print("nah")


s = 0
for part in t:
    vc,vl = getscore(part)
    y = 0
    sc,sl = [],[]
    while y < len(part):
        x = 0
        while x < len(part[0]):
            part[y][x] = swap(part[y][x])
            sc,sl = getscore(part)
            # new horizontal line or vertical line now exists
            if (any([(e not in vc) for e in sc]) or any([(e not in vl) for e in sl])):
                y,x = 999, 999
                sc = [e for e in sc if e not in vc]
                sl = [e for e in sl if e not in vl]
                break
            part[y][x] = swap(part[y][x])
            x+=1
        y+=1
    s += scorefroml(sc,sl)
print(s)
