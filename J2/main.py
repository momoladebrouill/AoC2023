f = open("input.txt", "r")

games = []
num = 0
su = 0

# 2 red cubes, 13 green cubes, and 14 blue cubes
for line in f.readlines(): # pour chaque game
    line = line.strip()
    num += 1 
    game = line[line.find(':')+2:].split(";")
    sets = []
    for st in game :
        sets.append(st.split(','))
    hmin = {'red' : 0,'blue':0,'green':0}
    for party in sets: # pour chaque party
        for sortie in party: # pour chaque couleur sortie dans la party
            sortie = (sortie[1:] if sortie.startswith(' ') else sortie)
            print(sortie)
            qqty,color = sortie.split(' ')
            qqty = int(qqty)
            if qqty > hmin[color] :
                hmin[color] = qqty
        print("nextparty")
    su+=hmin['red']*hmin['green']*hmin['blue']
print(su)
        
