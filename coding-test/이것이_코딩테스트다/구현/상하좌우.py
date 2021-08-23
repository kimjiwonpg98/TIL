N = int(input())

A = [1, 1]

move_plan = list(input().split())

for position in move_plan:
  if (position == "R"):
    if not A[1] == 5:
      A[1] += 1
  if (position == "L"):
    if not A[1] == 1:
      A[1] -= 1
  if (position == "U"):
     if not A[0] == 1:
        A[0] -= 1
  if (position == "D"):
    if not A[0] == 5:
      A[0] += 1

print(A[0], A[1])




# 다른 풀이

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in move_plan:
  i = move_types.index(plan)
  nx = x + dx[i]
  ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > N or ny > N:
    continue

  x, y = nx, ny

print(x, y)

