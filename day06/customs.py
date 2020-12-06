with open("input.txt") as f:
    data = f.read().split("\n\n")
    forms = [line.split("\n") for line in data]
part1 = 0
part2 = 0
for form in forms:
    answers = set("".join(form))
    part1 += len(answers)
    for answer in answers:
        if all(answer in line for line in form):
            part2 += 1

print(part1)
print(part2)
