C = int(input())

for i in range(C):
  scores = list(map(int, input().split(" ")))
  count = 0
  avg = (sum(scores, 0.0) - scores[0]) / scores[0]
  for j in range(1, scores[0]+1): 
    if (avg < scores[j]):
      count += 1
  result = round(count / (len(scores) - 1)*100, 3)

  print("{:.3f}%".format(result))