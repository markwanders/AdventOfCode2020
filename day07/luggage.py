import re

with open("input.txt") as f:
    data = f.readlines()
    parts = [line.split(" bags ") for line in data]
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


def traverse(bag, number_of_bags):
    additional_bags = 0
    for rule in rules[bag]:
        matches = re.findall("(?:contain|,) (.*?) (?:bag|bags)", rule)
        # print("%s, %s" % (bag, matches))
        for match in matches:
            if "no other" not in match:
                number = int(match[0])
                contained_bag = match[2:]
                additional_bags += traverse(contained_bag, number * number_of_bags)
    return number_of_bags + additional_bags


print(traverse("shiny gold", 1) - 1)
