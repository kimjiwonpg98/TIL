N,K = map(int, input().split())

numbers = []
result = []

for i in range(1, N + 1):
  numbers.append(i)

popNum = 0

while len(numbers) > 0:
  popNum = (popNum + (K - 1)) % len(numbers)
  number = numbers.pop(popNum)
  result.append(str(number))

print("<%s>" %(", ".join(result)))



    