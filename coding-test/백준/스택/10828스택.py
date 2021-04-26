import sys

class Stack(list):
  def __init__ (self):
        self.top = []

  def push(self, item):
    self.top.append(item)

  def pop(self):
    if not self.isEmpty():
      return print(self.top.pop(-1))
    else:
      print(-1)

  def isEmpty(self):
    return len(self.top) == 0

  def size(self):
    return print(len(self.top))

  def peak(self):
    if self.isEmpty():
      return print(-1)
    return print(self.top[-1])

  def empty(self):
    if len(self.top) == 0:
      return print(1)
    return print(0)

n = int(sys.stdin.readline())

result = Stack()

for i in range(n):
  order = list(sys.stdin.readline().split())
  if (order[0] == "push"):
    result.push(int(order[1]))
  if (order[0] == "pop"):
    result.pop()
  if (order[0] == "top"):
    result.peak()
  if (order[0] == "size"):
    result.size()
  if (order[0] == "empty"):
    result.empty()