import re

with open("input.txt") as f:
    parts = [line.split(" bags ") for line in f.readlines()]
    rules = {part[0]: part[1:] for part in parts}


def find_containing_colors(inner_bag, containing_colors):
    for outer_bag in rules.keys():
        if any(inner_bag in rule for rule in rules[outer_bag]):
            containing_colors.add(outer_bag)
            find_containing_colors(outer_bag, containing_colors)
    return containing_colors


print("Part 1 : %s" % len(find_containing_colors("shiny gold", set())))


def total_bags(bag, number_of_bags):
    additional_bags = 0
    for rule in rules[bag]:
        for match in re.findall("(?:contain|,) (.*?) (?:bag|bags)", rule):
            if "no other" not in match:
                number = int(match[0])
                contained_bag = match[2:]
                additional_bags += total_bags(contained_bag, number * number_of_bags)
    return number_of_bags + additional_bags


print("Part 2: %s " % (total_bags("shiny gold", 1) - 1))
