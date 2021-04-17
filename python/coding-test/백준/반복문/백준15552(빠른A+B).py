import sys
count = int(input())

numbers = []
for i in range(count): 
  x, y = map(int, sys.stdin.readline().split(" "))
  numbers.append(x+y)
  
for number in numbers: 
  print(number)