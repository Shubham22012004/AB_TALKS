lst = list(map(int,input().split()))
dit = dict()

#finding the sum
summ = 0
#finding the  maxi
maxi = float('-inf')
#finding the mini
mini = float('inf')
for x in lst:
  summ += x
  if(maxi < x):
    maxi = x
  if(mini > x):
    mini = x

print(summ)
print(maxi)
print(mini)

#counting frequency
for x in lst:
  if x in dit:
    dit[x] += 1
  else:
    dit[x] = 1

print(dit)