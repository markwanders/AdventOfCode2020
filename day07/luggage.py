with open("input.txt") as f:
    data = f.readlines()
    parts = [line.split(" bags") for line in data]
    rules = {part[0]: part[1:] for part in parts}

bags_to_find = ["shiny gold"]
found = True
while found:
    found = False
    for bag in rules.keys():
        for bag_to_find in bags_to_find:
            if any(bag_to_find in rule for rule in rules[bag]) and bag not in bags_to_find:
                bags_to_find.append(bag)
                found = True
print(len(bags_to_find) - 1)
