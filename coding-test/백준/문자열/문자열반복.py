T = int(input())

for i in range(T):
  cnt, word = input().split()
  
  for j in word:
    print(j * int(cnt), end='')
  print()