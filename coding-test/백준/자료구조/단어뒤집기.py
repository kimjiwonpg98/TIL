import sys

N = int(sys.stdin.readline())

for i in range(N):
  sentence = sys.stdin.readline()[::-1]
  store = sentence.split()
  store.reverse()
  sentence_reverse = ' '.join(store)
  print(sentence_reverse)