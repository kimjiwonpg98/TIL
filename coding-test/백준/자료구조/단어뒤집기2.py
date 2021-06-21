import sys

result = ''
reverse_word = ''
reverse = True
sentence = list(sys.stdin.readline().rstrip())

for word in sentence:
  if (word == ">"):
    reverse = True
    result += ">"
  elif (word == "<"):
    result += reverse_word[::-1]
    reverse_word = ''
    result += "<"
    reverse = False
  elif (word == " "):
    result += reverse_word[::-1]
    result += word
    reverse_word = ''
  elif (reverse == False):
    result += word
  elif (reverse == True):
    reverse_word += word
  

if (len(reverse_word) != 0):
    result += reverse_word[::-1]
    reverse_word = ''


print(result)