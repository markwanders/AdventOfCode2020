with open("input.txt") as f:
    start_time = int(f.readline())
    busses = f.readline().split(",")


def part1():
    wait_time = 0
    while True:
        for bus in [int(b) for b in busses if b.isdigit()]:
            if (start_time + wait_time) % bus == 0:
                return bus * wait_time
        wait_time += 1


print(part1())
