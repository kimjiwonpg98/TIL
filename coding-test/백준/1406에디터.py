import sys
# sys는 \n까지 저장 strip()붙여주자
word = list(sys.stdin.readline().strip())
word_stack = []
order_length = int(sys.stdin.readline())
word_length = len(word)
cursor = word_length

for i in range(order_length):
  order = sys.stdin.readline().split()
  
  if order[0] == "L" and word != []:
    word_stack.append(word.pop())

  if order[0] == "D" and word_stack != []:
    word.append(word_stack.pop())

  if order[0] == "B" and word != []:
    word.pop()

  if order[0] == "P":
    word.append(order[1])

result = word + list(reversed(word_stack))

print(''.join(result))