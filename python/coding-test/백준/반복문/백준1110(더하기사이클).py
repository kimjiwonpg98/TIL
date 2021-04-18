number = int(input());

first = number

result = 0;

while 1:
  result += 1
  num = number // 10 + number % 10
  new_num = (number % 10)*10 + num % 10
  number = new_num
  if (new_num == first): break

print(result)