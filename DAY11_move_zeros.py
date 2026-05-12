def fun(lst):
  if(len(lst) == 1):
    return lst
  
  
  i=0
  j=1
  while j<len(lst):
    if(lst[j]==0):
      j+=1
    elif(lst[i] != 0):
      i+=1
    else:
      lst[i],lst[j] = lst[j], lst[i]
      j+=1
    
    
  return lst


lst = list(map(int, input("enter the list element : ").split()))
print(fun(lst))