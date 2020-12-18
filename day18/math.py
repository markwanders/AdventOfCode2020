import re

with open("input.txt") as f:
    lines = f.read().splitlines()


def calc(input):
    result = 0
    operator = None
    pattern = r"(\([0-9+\* ]*\))"
    match = re.search(pattern, input)
    while match is not None:
        to_calc = match.group(1)[1:-1]
        input = input.replace(match.group(1), str(calc(to_calc)))
        match = re.search(pattern, input)

    for char in input.split(" "):
        if char.isdigit():
            if operator is None:
                result = int(char)
            elif operator == "*":
                result *= int(char)
            elif operator == "+":
                result += int(char)
        else:
            operator = char
    return result


def part1():
    print(sum([calc(l) for l in lines]))


part1()
