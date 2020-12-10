with open("input.txt") as f:
    data = [int(s) for s in f.readlines()]
    data.append(max(data) + 3)
    data.append(0)
    data.sort()

one = 0
three = 0
current = 0
for adapter in data:
    if adapter - current == 1:
        one += 1
    if adapter - current == 3:
        three += 1
    current = adapter
print(one, three, one * three)

paths = {}

data.sort()
for adapter in data:
    if adapter == min(data):
        paths[adapter] = 1
    else:
        paths[adapter] = paths.get(adapter - 1, 0) + paths.get(adapter - 2, 0) + paths.get(adapter - 3, 0)
print(max(paths.values()))
