with open("input.txt") as f:
    lines = f.read().splitlines()

part1, part2 = 0, 0
for line in lines:
    parts = line.split(" ")
    policy = parts[0].split("-")
    character = parts[1][0]
    password = parts[-1]
    occurrences = password.count(character)
    if int(policy[0]) <= occurrences <= int(policy[-1]):
        part1 += 1
    if password[int(policy[0]) - 1] == character and not password[int(policy[-1]) - 1] == character:
        part2 += 1
    elif password[int(policy[-1]) - 1] == character and not password[int(policy[0]) - 1] == character:
        part2 += 1

print part1
print part2
