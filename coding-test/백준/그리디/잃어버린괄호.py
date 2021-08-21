formula = input()
result = 0
minus_numbers = list()
plus_numbers = list(formula.split("-"))

for number in plus_numbers:
  if ("+" in number):
    num = list(map(int, number.split("+")))
    minus_numbers.append(sum(num))
  else:
    minus_numbers.append(int(number))

for i in range(len(minus_numbers)):
  if (i == 0):
    result += minus_numbers[i]
  else:
    result -= minus_numbers[i]

print(result)