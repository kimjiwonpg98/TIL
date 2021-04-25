rest = []

for i in range(1, 11):
  number = int(input())
  rest.append(number % 42)

set_rest = set(rest)
rest = list(set_rest)

print(len(rest))