with open("input.txt") as f:
    data = [int(s) for s in f.readlines()]

part1 = 0
for i in range(25, len(data)):
    preamble = data[i - 25:i]
    if any(j + k == data[i] and j != k for j in preamble for k in preamble):
        continue
    else:
        part1 = data[i]
        break
print(part1)

for i in range(0, len(data)):
    sequence = []
    while sum(sequence) < part1:
        sequence.append(data[i + len(sequence)])
    if sum(sequence) == part1:
        print(min(sequence) + max(sequence))
        break

