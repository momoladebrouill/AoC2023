from pprint import pprint
f = open("input.txt", "r")
parcour = f.readline()
f.readline()
jumps = {}
for line in f.readlines():
    x,y=line.split("=")
    jumps[x.strip()] = [e.strip() for e in y[2:-2].split(',')]
currents = [ values for values in jumps.keys() if values.endswith("A")]

def getlength(current):
    i = 0
    instru = 0
    while not current.endswith("Z"):
        current = jumps[current][0 if parcour[instru] == 'L' else 1]
        instru += 1
        instru = instru %(len(parcour)-1)
        i+=1
    return i

lengths = [getlength(c) for c in currents]
print(lengths)

