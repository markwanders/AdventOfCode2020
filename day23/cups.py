from collections import deque

with open("input.txt") as f:
    cups = [int(c) for c in f.readline()]


def part1(cups):
    for _ in range(100):
        current_value = cups[0]
        cups.rotate(cups.index(current_value) - 1)
        pickup = [cups.popleft()] + [cups.popleft()] + [cups.popleft()]
        destination_value = current_value - 1
        while destination_value not in cups:
            destination_value -= 1
            if destination_value < min(cups):
                destination_value = max(cups)
        destination = cups.index(destination_value)
        pickup.reverse()
        for p in pickup:
            cups.insert(destination + 1, p)
    cups.rotate(-cups.index(1))
    print("".join([str(c) for c in cups][1:]))


part1(deque(cups))


class Link:
    def __init__(self, value):
        self.value = value
        self.next = None


def part2(cups):
    cup_range = int(1e6)
    links = {}

    for c in range(1, cup_range + 1):
        links[c] = Link(c)

    for a, b in zip(cups, cups[1:]):
        links[a].next = links[b]

    links[cups[-1]].next = links[len(cups) + 1]
    for i in range(len(cups) + 1, cup_range):
        links[i].next = links[i + 1]
    links[cup_range].next = links[cups[0]]

    current = links[cups[0]]

    for _ in range(int(1e7)):
        pickup_start = current.next
        pickup_end = current.next.next.next
        pickup = [pickup_start.value, pickup_start.next.value, pickup_end.value]
        destination = current.value - 1 if current.value > 1 else cup_range
        while destination in pickup:
            destination -= 1
            if destination == 0:
                destination = cup_range

        current.next = pickup_end.next
        pickup_end.next = links[destination].next
        links[destination].next = pickup_start

        current = current.next
    print(links[1].next.value * links[1].next.next.value)


part2(cups.copy())
