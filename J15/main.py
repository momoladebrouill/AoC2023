from pprint import pprint
f = open("input.txt","r")

t = f.readline().strip().split(',')
def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v*=17
        v = v %256
    return v
boxes = [ [] for i in range(255) ]
for v in t:
    print(v)
    try:
        i = v.index('=')
    except ValueError:
        i = v.index('-')
    name = v[:i]
    box,instru = h(name),v[i:]
    box = boxes[box]
    # si il y est, on l'enlève
    if instru == '-':
        for i in range(len(box)):
            if box[i][0] == name:
                box.pop(i)
                break
    else:
        qqty = v[i+1:]
        done = False
        for i in range(len(box)):
            if box[i][0] == name:
                box[i][1] = qqty
                done = True
                break
        if not done:
            box.append([name,qqty])
    '''for i,b in enumerate(boxes):
        if b!= []:
            print(i,b)
    print('--- new instruction --')'''
s = 0
for j,box in enumerate(boxes):
    for i,elem in enumerate(box):
        s += (i+1) * int(elem[1]) * (j+1)
print(s)
