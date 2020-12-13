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


def part2():
    t = 0
    step = 0
    previous_bus = 0
    previous_offset = 0
    for bus in [int(b) for b in busses if b.isdigit()]:
        offset = busses.index(str(bus))
        if previous_bus > 0:
            while (t + offset) % bus != 0 or (t + previous_offset) % previous_bus != 0:
                t += step
            step *= bus
        else:
            step = bus
        previous_bus, previous_offset = bus, offset
    return t


print(part2())
