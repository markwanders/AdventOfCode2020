from collections import deque

with open("input.txt") as f:
    cups = deque([int(c) for c in f.readline()])

for i in range(100):
    current_value = cups[0]
    # print("--- Move %s ---" % (i + 1))
    # print("Current cup is %s, list is %s" % (current_value, cups))
    cups.rotate(cups.index(current_value) - 1)
    pickup = [cups.popleft()] + [cups.popleft()] + [cups.popleft()]
    # print("Picked up %s, list is %s" % (pickup, cups))
    destination_value = current_value - 1
    while destination_value not in cups:
        destination_value -= 1
        if destination_value < min(cups):
            destination_value = max(cups)
    destination = cups.index(destination_value)
    # print("Destination cup %s at %s" % (destination_value, destination))
    pickup.reverse()
    for p in pickup:
        cups.insert(destination + 1, p)
    # print("Inserted cups, list is now %s" % cups)
    current = cups.index(current_value) + 1
cups.rotate(-cups.index(1))
print("".join([str(c) for c in cups][1:]))
