import sys

N = int(sys.stdin.readline())
stack = []
output = []
stack_count = 0
success = True

for i in range(N):
  number = int(sys.stdin.readline())
  while stack_count < number:
      stack_count += 1
      stack.append(stack_count)
      output.append("+")

  if stack[-1] == number:
    stack.pop()
    output.append("-")
  else:
    success = False
    break
      
if success:
  for i in output:
    print(i)
else:
  print("NO")
    
