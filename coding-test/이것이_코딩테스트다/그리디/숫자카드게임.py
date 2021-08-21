N, M = map(int, input().split())

result = 0

for i in range(N):
  data = map(int, input().split())

  min_num = min(data)
  result = max(result, min_num)

print(result)