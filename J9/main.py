from pprint import pprint
f = open("input.txt", "r")
p = []
for line in f.readlines():
    l = [int(e) for e in line.strip().split(' ')]
    k = [l]
    while not all([e == 0 for e in k[-1]]):
        l = k[-1]
        nl = []
        for i in range(len(l)-1):
            nl.append(l[i+1]-l[i])
        k.append(nl)
    for i in range(len(k)-1,0,-1):
        k[i-1] = [k[i-1][0] - k[i][0]] + k[i-1]
    p.append(k)
pprint(p)
print(sum(k[0][0] for k in p))
            

