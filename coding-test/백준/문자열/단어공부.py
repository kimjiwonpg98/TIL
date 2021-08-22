word = input()

word = word.upper()
alphabets = {}

for alphabet in word:
  if alphabet in alphabets:
    alphabets[alphabet] += 1
  else:
    alphabets[alphabet] = 1

most_alphabet = [k for k, v in alphabets.items() if v == max(alphabets.values())]

if len(most_alphabet) == 1:
  print(most_alphabet[0])
else:
  print("?")