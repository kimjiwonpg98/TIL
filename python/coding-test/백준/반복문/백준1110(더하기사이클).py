number = input();

if (int(number) < 9): number = number + str(0)
first = number;
result = 0;

while 1:
  x = int(number[0])
  y = int(number[1])
  result += 1
  sum = x + y

  if (sum > 9 ): z = str(sum % 10)
  else: z = str(sum)

  number = str(y) + z
  if (number == first): break

print(result)