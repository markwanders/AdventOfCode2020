import re

with open("input.txt") as f:
    parts = f.read().split("\n\n")
fields = dict()
allowed_numbers = set()
for line in parts[0].split("\n"):
    match = re.findall("^([a-z ]*): ([0-9-]*) or ([0-9-]*)$", line)[0]
    range1 = [int(i) for i in match[1].split("-")]
    range2 = [int(i) for i in match[2].split("-")]
    allowed_numbers.update(set(range(range1[0], range1[1] + 1)))
    allowed_numbers.update(set(range(range2[0], range2[1] + 1)))
    fields[match[0]] = ([int(i) for i in match[1].split("-")], [int(i) for i in match[2].split("-")])

print(allowed_numbers)
errors = []
for line in parts[2].split("\n"):
    if "nearby tickets" in line:
        continue
    numbers = [int(i) for i in line.split(",")]
    for number in numbers:
        if number not in allowed_numbers:
            errors.append(number)
print(sum(errors))
