N = int(input())

count = 1
distance = list(map(int, input().split()))
city_cost = list(map(int, input().split()))

cost = distance[0] * city_cost[0]
min_cost = city_cost[0]

while count < N - 1:
  if (min_cost <= city_cost[count]):
    cost += min_cost * distance[count]
  else:
    cost += city_cost[count] * distance[count]
    min_cost = city_cost[count]
  count += 1

print(cost)



# for i in range(1, N):
#   if (i == N - 1): break
#   if (min_cost <= city_cost[i]):
#     cost += min_cost * distance[i]
#   else:
#     cost += city_cost[i] * distance[i]
#     min_cost = city_cost[count]

# print(cost)