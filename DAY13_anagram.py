#mehod 1 -> Brute Force Apporach, making two dictinary and then compare the charater count
def checkAnagram(st1, st2):
  if len(st1) != len(st2):
    return False
  
  dict1 = dict()
  dict2 = dict()
  for i in st1:
    if i in dict1:
      dict1[i]+=1
    else:
      dict1[i] = 1

  for i in st2:
    if i in dict2:
      dict2[i]+=1
    else:
      dict2[i] = 1

  if len(dict1) != len(dict2):
    return False
  for i in dict1:
    if i not in dict2:
      return False
    if i in dict2 and dict1[i] != dict2[i]:
      return False
  return True

#method2 -> Optimal approach, using single dictonary

def checkAnagram2(st1, st2):
  if len(st1) != len(st2):
    return False
  
  dict1 = dict()
  
  for i in st1:
    if i in dict1:
      dict1[i]+=1
    else:
      dict1[i] = 1

  for i in st2:
    if i in dict1:
      dict1[i]-=1

  for i in dict1:
    if dict1[i] != 0:
      return False
  return True 


s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")
print(checkAnagram(s1,s2))
print(checkAnagram2(s1,s2))