try:
  marks = int(input())
  if marks > 90 and marks<=100:
    print('A')
  elif marks > 75 and marks<=90:
    print('B')
  elif marks > 50 and marks <=75:
    print('C')
  else:
    print("Fail")

except:
  print("Invalid input")
