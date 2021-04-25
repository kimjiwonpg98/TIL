count = int(input())

numbers = []
for i in range(count):
  x, y = map(int, input().split(" "))
  numbers.append(x+y)
  
for number in numbers: 
  print(number)


#A+B - 4

while (1):
  try:
    x, y = map(int, input().split(" "))
    print(x+y)
  except:
    break