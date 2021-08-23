N = input()

hour_count = 0
min_count = 0
sec_count = 0

for hour in range(24):
  if (N in str(hour)):
    hour_count += 1
  for min in range(60):
    if (N in str(min)):
      min_count += 1
    for sec in range(60):
      if (N in str(sec)):
        sec_count += 1

print(hour_count + min_count + sec_count)

# ㅎㅎ 잘못 했다...


count = 0

for hour in range(int(N) + 1):
  for min in range(60):
    for sec in range(60):
     if '3' in str(hour) + str(min) + str(sec):
       count += 1

print(count)