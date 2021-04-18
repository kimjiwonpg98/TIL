N = int(input())

for i in range(N):
  quiz = input()
  result = 0
  counter = 0
  for j in range(len(quiz)):
    if quiz[j] == "O":
      counter += 1
      result = result + counter
    else: 
      counter = 0
  print(result)
