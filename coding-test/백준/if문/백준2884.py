H, M = map(int, input().split(" "));

if (M < 45):
  H = H - 1
  if (H == -1): 
    H = 23
  M = 60 + (M - 45)
else: 
  M = M - 45

print("{} {}".format(H,M));