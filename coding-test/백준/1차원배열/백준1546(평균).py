N = int(input())
numbers = list(map(int, input().split()))

M = max(numbers)
avg_score = 0

for i in range(len(numbers)):
  numbers[i] = numbers[i] / M * 100
  avg_score += numbers[i]

result = avg_score / len(numbers)
print(result)
