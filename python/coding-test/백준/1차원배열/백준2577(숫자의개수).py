number = 1
numbers = [0,0,0,0,0,0,0,0,0,0]
for i in range(1, 4):
  number = number * int(input())

number = list(map(int, str(number)))

for i in number:
  numbers[i] += 1

for i in numbers:
  print(i)