try:
  lst = list(map(int,input("enter the elements : ").split()))
  counter = 0
  for x in lst:
    if x%2==0:
      counter+=1
  print(counter)

except:
  print("invalid inputs")