numbers = []

for i in range(1, 10):
    numbers.append(int(input()))


print(max(numbers))
print(numbers.index(max(numbers)) + 1)