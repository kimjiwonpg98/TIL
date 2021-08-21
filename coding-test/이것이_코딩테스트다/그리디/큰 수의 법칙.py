N, M, K = map(int, input().split(" "))

numbers = list(map(int, input().split(" ")))

numbers.sort()
result, count = [0, 0]


first = numbers[N - 1]
second = numbers[N - 2]

while True:
  
  for i in range(K):
    result += first
    count += 1

  if (count < M):
    result += second
    count += 1

  if (count == M): break


print(result)



# 다른 풀이

# count = (M // (K + 1)) * K
# count += M % (K + 1)

# result = 0
# result += count * first
# result += (M - count) * second