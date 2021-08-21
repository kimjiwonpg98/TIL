N, K = map(int, input().split())

price = list()
count = 0

for i in range(N):
  price.append(int(input()))

price.sort(reverse=True)

for money in price:
  money_count = K // money
  K -= money * money_count
  count += money_count

print(count)