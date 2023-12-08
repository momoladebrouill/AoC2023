from pprint import pprint
f = open("input.txt", "r")



class Interval:
    # debut et fin inclu
    def __init__(self,deb,size):
        self.deb = deb
        self.size = size
    @property
    def debut(self):
        return self.deb
    @property
    def fin(self):
        return self.deb + self.size - 1
    def __repr__(self):
        return f'[{self.deb};{self.size}]'
def fu(deb,fin):
    return Interval(deb,fin-debut)
trucs = [int(e) for e in f.readline().split(":")[-1].strip().split(" ")]
# trucs = list(map(int, f.readline().split(":")[-1].strip().split("")))
intervals = []
for i in range(0,len(trucs)-1,2):
    intervals.append(Interval(trucs[i],trucs[i+1]))
seeds = intervals
nseeds = len(seeds)
maps = f.read().strip().split("\n\n")
def dist(a,b):
    return abs(a - b) - 1
for map_ in maps:
    print("nouvelle transformation ----")
    newseeds = []
    for line in map_.split(":")[-1].strip().split("\n"): # pour chaque filtre
        dst,src,range_ = [int(e) for e in line.strip().split(" ")]
        print(src,range_)
        nextfactory = []
        for i in seeds:
            # 1
            # ---- INTERVALLE
            #   ----- SRC/DST
            print(i)
            if i.debut < src and src <= i.fin < src+range_:
                newseeds.append(Interval(dst,dist(src,i.fin)))
                nextfactory.append(Interval(i.debut,dist(i.debut,src-1)))
                print("cas 1")
            # 2
            #    ---- INTERVALLE  
            # ----    SRC->DST
            elif src < i.debut <= src + range_ and src + range_ < i.fin:
                newseeds.append(Interval(dst + dist(i.debut,src),dist(i.debut+1, src + range_+1)))
                nextfactory.append(Interval(src+range_,dist(i.fin,src+range_+1)))
                print("cas 2")
            # 3
            #  --------- INTERVALLE
            #    ---- SRC -> DST
            elif i.debut < src and src+range_ < i.fin:
                newseeds.append(Interval(dst,range_))
                nextfactory.append(Interval(i.debut,dist(src-1,i.deb)))
                nextfactory.append(Interval(src+range_+1,dist(i.fin,src+range_+1)))
                print("cas 3")
            # 4
            #   ----
            #  -----------
            elif src <= i.debut and  i.debut + i.size <src + range_:
                newseeds.append(Interval(dst + dist(i.debut,src)+1,i.size))
                print("cas 4")
            # 5 et 6
            # ----       |        -----
            #      ----- | ------

            elif i.fin < src or src + range_ < i.debut:
                nextfactory.append(i)
                print("cas 5/6")
            # 5 et 6
            else:
                print("forgotten case",src,range_, i)
        seeds = nextfactory[:]
        print("newseeds",newseeds,"nextfactory",nextfactory)
    seeds = newseeds[:] + nextfactory[:]
    seeds.sort(key = lambda e: e.deb)
    print("seeds",seeds,"-------------")
print(min([e.deb for e in seeds]))
