try:

 
  lst = list(map(int,input("enter the list :").split()))
  summ = lst[0]
  maxi = lst[0]
  for x in lst[1:]:
    summ += x

    if summ > maxi:
      maxi = summ
    if summ < 0:
      summ = 0

  print(maxi)

except:
  print("invalid entry")