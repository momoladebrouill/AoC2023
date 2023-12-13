from pprint import pprint
f = open("ex.txt","r")

lines = [[part for part in lines.strip().split(" ")] for lines in f.readlines()]
for line in lines:
    line[1] = [int(e) for e in line[1].split(",")]

# on suppose que y a pas de '?'
def good(l,nums):
    hast = [e for e in l.split('.') if e!='']
    return len(hast) == len(nums) and all([nums[i] == len(hast[i]) for i in range(len(nums))])
def g(l):
    return ''.join(l)

def verif(doc,nums):
    l = [len(e) for e in doc.split('.') if e!='']
    for i in range(len(nums)):
        if i >= len(l):
            return True
        if l[i] < nums[i]:
            return False
'''
def essai(doc,nums):
    try:
        i = doc.index('?')
        if verif(''.join(doc[:i]),nums) == False:
            return 0
        s = 0
        doc[i] = '.'
        v = essai(doc[:],nums)
        s+=v

        doc[i] = '#'
        v = essai(doc[:],nums)
        s+=v
        return s
    except ValueError:
        return 1 if good(g(doc),nums) else 0
'''

def essai(doc,nums):
    l = [e for e in doc.split(".") if e!='']
    
s=0
for line in lines:
    doc,nums = line
    val = essai(list('?'.join(doc for _ in range(5))),sum((nums for _ in range(5)),start=[]),{})
    print(val)
    s+=val
print("solution",s)

