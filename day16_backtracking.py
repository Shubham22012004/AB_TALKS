

def subsets(nums):
    
  result = []

  def rec(i,arr):
      if i==len(nums):
          result.append(arr[:])
          return 

      # result.append(arr[:])

      arr.append(nums[i])
      rec(i+1, arr)
      arr.pop()
      rec(i+1, arr)
  
  rec(0,[])
  return result
        
num = [1,2,3]
print(subsets(num))