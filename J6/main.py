from pprint import pprint
f = open("input.txt", "r")

time = f.readline().split(':')[-1]
'''
times = [int(e.strip()) for e in f.readline().split(':')[-1].strip().split('  ') if e not in ['',' ']]
distances = [int(e.strip()) for e in f.readline().split(':')[-1].strip().split('  ') if e not in ['',' ']]
'''
time = 71530
distance =   940200
'''time = 35696887
distance = 213116810861248'''
i = 0
for hold in range(1,time):
    parcouru = (time-hold) * hold
    if parcouru > distance :
        i+=1
print(i)
# v = d/T
# d = v T 
