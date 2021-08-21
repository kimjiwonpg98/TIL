N = int(input())

conferences = list()
count = 1

for info in range(N):
  conferences.append(list(map(int, input().split())))

conferences.sort(key=lambda x: (x[1], x[0]))
end_time = conferences[0][1]

for i in range (1, N):
  if (conferences[i][0] >= end_time):
    count += 1
    end_time = conferences[i][1]

print(count)