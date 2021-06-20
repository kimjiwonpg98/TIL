from collections import deque
import sys

order_length = int(sys.stdin.readline())

result = deque()

for i in range(order_length):
  order = sys.stdin.readline().split()
  if (order[0] == "push_front"):
    result.appendleft(int(order[1]))
  if (order[0] == "push_back"):
    result.append(int(order[1]))
  if (order[0] == "pop_front"):
    if len(result) != 0:
      print(result[0])
      result.popleft()
    else: 
      print(-1)
  if (order[0] == "pop_back"):
    if len(result) != 0:
      print(result[len(result) - 1])
      result.pop()
    else: 
      print(-1)
  if (order[0] == "size"):
    print(len(result))
  if (order[0] == "empty"):
    print(1) if len(result) == 0 else print(0)
  if (order[0] == "front"):
    print(result[0]) if len(result) != 0 else print(-1)
  if (order[0] == "back"):
    print(result[len(result) -1]) if len(result) != 0 else print(-1)
