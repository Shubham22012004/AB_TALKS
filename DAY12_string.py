#reverse the string
st = input()

#method 1 -> using built-in  slicing method
st = st[::-1]
print(st)


#method 2 -> using extra space and a vriable
newSt = ''
while i<len(st):
  newSt = st[i]+newSt
  i+=1

print(newSt)