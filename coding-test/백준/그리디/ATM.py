N = int(input())

time = 0
each_time = list()
people = list(map(int, input().split()))

people.sort()

for user in people:
  time += user
  each_time.append(time)

result = sum(each_time)
print(result)