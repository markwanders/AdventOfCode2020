with open("input.txt") as f:
    start_time = int(f.readline())
    busses = f.readline().split(",")

next_bus = 0
wait_time = 0
while True:
    for bus in [int(b) for b in busses if b.isdigit()]:
        if (start_time + wait_time) % bus == 0:
            next_bus = bus
            break
    if next_bus > 0: break
    wait_time += 1
print(wait_time * next_bus)
