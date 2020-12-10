with open("input.txt") as f:
    data = [int(s) for s in f.readlines()]
    data.sort()

one = 0
three = 1
current = 0
for index, adapter in enumerate(data):
    if adapter - current == 1:
        one += 1
    if adapter - current == 3:
        three += 1
    current = adapter
print(one, three, one * three)
