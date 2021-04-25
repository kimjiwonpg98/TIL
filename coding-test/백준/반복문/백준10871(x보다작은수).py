n, x = map(int, input().split(" "))
y = input().split(" ")

for i in range (len(y)): 
  if x > int(y[i]): print(y[i], end=" ")

