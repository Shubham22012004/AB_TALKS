st_list = ["(({{]}{}}(())[[]]))[", "{{(})}{{()}}   ", "", "{{}()}[[]]" ]


result=[]
for st in st_list:
  st = st.strip()
  lst = []
  if not st:
    result.append("Not bracket string")
    continue
  for i in st:
    
    if i in "})]":
      if lst[len(lst)-1] == '[' and i==']':
        lst.pop()
      elif lst[len(lst)-1] == '{' and i=='}':
        lst.pop()
      elif lst[len(lst)-1] == '(' and i==')':
        lst.pop()
      else:
        lst.append(i)
    else:
      lst.append(i)
    
  if lst:
    result.append("Not valid sequence")
  else:
    result.append("valid sequence")

print(result)