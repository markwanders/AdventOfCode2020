import re

with open("input.txt") as f:
    lines = f.read().splitlines()


def calc(input, add_precedence):
    result = 0
    operator = None
    pattern = r"(\([0-9+\* ]*\))"
    match = re.search(pattern, input)
    while match is not None:
        input = input.replace(match.group(1), str(calc(match.group(1)[1:-1], add_precedence)))
        match = re.search(pattern, input)
    if add_precedence:
        add_pattern = r"([0-9]+ \+ [0-9]+)"
        add_match = re.search(add_pattern, input)
        while add_match is not None:
            input = input.replace(add_match.group(1), str(calc(add_match.group(1), False)))
            add_match = re.search(add_pattern, input)
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
    print(sum([calc(line, False) for line in lines]))


def part2():
    print(sum([calc(line, True) for line in lines]))


part1()
part2()
