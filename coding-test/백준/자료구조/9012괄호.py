import sys

N = int(sys.stdin.readline())

for i in range(N):
  is_vps = sys.stdin.readline()
  is_vps = is_vps.replace("()","")
  while(True):
      if (is_vps.find("()") != -1):
        is_vps = is_vps.replace("()","")
      else:
        break
  if is_vps.find("(") != -1 or is_vps.find(")") != -1:
    print("NO")
  else:
    print("YES")