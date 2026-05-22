#solving recursion problem -> count the consonant in the string using recursion

def fun(st, index):
  if index == len(st):
    return 0
  if st[index] in 'aeiouAEIOU':
    return 0 + fun(st,index+1)  
  return fun(st,index+1)+1

st = input("enter the string : ")
print(fun(st,0))


#solving stack prblem -> next greater element in array

def nextLargerElement(arr):
    n = len(arr)
    result = [-1] * n  

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result

arr = [12,43,76,9,23,53,60,6]
result = nextLargerElement(arr)
print(result)