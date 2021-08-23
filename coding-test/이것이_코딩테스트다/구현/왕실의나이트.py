position = list(input())
count = 0
vitural = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

steps = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in vitural:
  if i == position[0]:
    x = vitural.index(i) + 1

y = int(position[1])

for step in steps:
  nx = x + step[0]
  ny = y + step[1]

  if nx > 0 and ny > 0 and nx < 9 and ny < 9:
    count += 1


print(count)