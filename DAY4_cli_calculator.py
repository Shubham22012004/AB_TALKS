a = int(input())
b = int(input())
operator = input()

match(operator):
  
  case '+':
    print(a+b)
  case '-':
    print(a-b)

  case '*':
    print(a*b)
  case '/':
    try:
      print(a/b)
    except ZeroDivisionError:
      print("can not divisible by zero")
  
