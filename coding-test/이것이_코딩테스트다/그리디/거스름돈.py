money = int(input())
count = 0

exchange_list = [500, 100, 50, 10]

for coin in exchange_list:
  count += money // coin
  money %= coin

print(count)