with open("input.txt") as f:
    data = [int(s) for s in f.readlines()]

for i in range(25, len(data)):
    preamble = data[i-25:i]
    if any(j + k == data[i] and j != k for j in preamble for k in preamble):
        continue
    else:
        print(data[i])
        break

