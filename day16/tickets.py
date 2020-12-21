import re
from functools import reduce
import operator

with open("input.txt") as f:
    parts = f.read().split("\n\n")
fields = dict()
allowed_numbers = set()
for line in parts[0].split("\n"):
    match = re.findall("^([a-z ]*): ([0-9-]*) or ([0-9-]*)$", line)[0]
    range1 = [int(i) for i in match[1].split("-")]
    range2 = [int(i) for i in match[2].split("-")]
    fields[match[0]] = set(range(range1[0], range1[1] + 1))
    fields[match[0]].update(set(range(range2[0], range2[1] + 1)))
    allowed_numbers.update(fields[match[0]])
tickets = parts[2].split("\n")[1:]
your_ticket = [int(i) for i in parts[1].split("\n")[-1].split(",")]


def part1():
    errors = []
    for ticket in tickets:
        for number in [int(i) for i in ticket.split(",")]:
            if number not in allowed_numbers:
                errors.append(number)
    print(sum(errors))


def part2():
    valid_tickets = []
    for ticket in tickets:
        if all(number in allowed_numbers for number in [int(i) for i in ticket.split(",")]):
            valid_tickets.append(ticket)
    possibilities = [list(fields.keys()) for _ in range(len(fields.keys()))]
    for ticket in valid_tickets:
        for i, number in enumerate([int(i) for i in ticket.split(",")]):
            for field, field_range in fields.items():
                if number not in field_range:
                    possibilities[i].remove(field)
    actual_fields = ["empty"] * len(fields.keys())
    while "empty" in actual_fields:
        for i, possibility in enumerate(possibilities):
            for field in possibility:
                if [p for sublist in possibilities for p in sublist].count(field) == 1 and field not in actual_fields:
                    actual_fields[i] = field
                    possibilities[i] = []
                    break
    print(reduce(operator.mul, [value for (i, value) in enumerate(your_ticket) if "departure" in actual_fields[your_ticket.index(value)]], 1))


part1()
part2()
