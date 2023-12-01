f = open("input.txt", "r")

su = 0

nums = ["zero","one", "two", "three", "four", "five", "six", "seven","eight","nine"] + [str(i) for i in range(0,10)]
def convert(num):
    return nums.index(num)%10


for l in f.readlines():
  l = l.strip()
  print(l)
  l = l + ' '
  tokens = []
  i = 0
  while i < len(l)  :
    found = False
    for num in nums:
        if l[i:].startswith(num):
            tokens.append(convert(num))
            found = True
    i+=1

  trucs = tokens
  print(trucs)
  if len(trucs)>0 : 
    v = int(str(trucs[0])+str(trucs[-1]))
  print(v)
  print()
  su += v
print(su)
print(nums)

