import re

with open("input.txt") as f:
    lines = f.read().splitlines()


def calc(problem, add_precedence):
    result = 0
    operator = None
    pattern = r"(\([0-9+\* ]*\))"
    match = re.search(pattern, problem)
    while match is not None:
        problem = problem.replace(match.group(1), str(calc(match.group(1)[1:-1], add_precedence)), 1)
        match = re.search(pattern, problem)
    if add_precedence:
        add_pattern = r"([0-9]+ \+ [0-9]+)"
        add_match = re.search(add_pattern, problem)
        while add_match is not None:
            problem = problem.replace(add_match.group(1), str(calc(add_match.group(1), False)), 1)
            add_match = re.search(add_pattern, problem)
    for char in problem.split(" "):
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
