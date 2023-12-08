from pprint import pprint
f = open("input.txt", "r")
#hand, bid
hands = [line.split() for line in f.readlines()]

# première valeur = plus forte
values =  [str(e) for e in ['A', 'K', 'Q', 'T', 9, 8, 7, 6, 5, 4, 3, 2, 'J']]

def maping(e):
    return "123456789ABCDEF"[values.index(e)]
    
# 247889944
# 247433527
def sorting(hand):
    cards = hand[0]
    qqty = {}
    for card in cards:
        if card in qqty:
            qqty[card] += 1
        else:
            qqty[card] = 1
    m = (0,0) # carte qui revient le plus de fois
    if 'J' in qqty:
        qqty['J'] *= -1
    for key in qqty:
        if qqty[key] > m[1] :
            m = key,qqty[key]
    if cards == 'JJJJJ':
        qqty['J'] = 5
    elif 'J' in qqty:
        qqty[m[0]] += -qqty['J']
    # five of a kind
    #print(cards,qqty,shift)
    rank = ''.join([maping(e) for e in cards])
    if 5 in qqty.values():
        return 'a' + rank
    if 4 in qqty.values():
        return 'b' + rank
    if 3 in qqty.values() and 2 in qqty.values():
        return 'c' + rank
    if 3 in qqty.values() and not (2 in qqty.values()):
        return 'd' + rank
    if 2 in qqty.values():
        l = list(qqty.values())
        l.pop(l.index(2))
        if 2 in l:
            return 'e' + rank
        else:
            return 'f' + rank
    if all([q == 1 for q in qqty.values()]): 
        return 'g' + rank
    print("Error",cards,qqty,shift)
# sort by first element
sort = sorted(hands, key = sorting,reverse = True)
print(sort)
print([sorting(key) for key in sort])
s = 0
i = 1
for e in sort:
    s+=i * int(e[1])
    i+=1
print(s)
'''
test = [('77888',2),('77788',1)]
print(sorted(test, key = sorting, reverse = True))
print([sorting(key) for key in test])
'''
