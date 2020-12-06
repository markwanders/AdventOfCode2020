import string

with open("input.txt") as f:
    data = f.read().split("\n\n")
    answers = [line.split("\n") for line in data]
total = 0
for answer in answers:
    total += len(set(string.join(answer, "")))
print total