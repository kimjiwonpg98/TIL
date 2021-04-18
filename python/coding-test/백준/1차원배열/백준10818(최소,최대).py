count = int(input());

numbers = list(map(int, input().split(" ")))

min = min(numbers)
max = max(numbers)

print("{} {}".format(min, max))