with open("input.txt") as f:
    lines = f.readlines()

facing = 0
position = (0, 0)
for instruction in lines:
    action = instruction[0]
    value = int(instruction[1:])
    if action == "F":
        x, y = 0, 0
        if facing == 0:
            x = 1
        elif facing == 90:
            y = -1
        elif facing == 180:
            x = -1
        elif facing == 270:
            y = 1
        position = (position[0] + value * x, position[1] + value * y)
    elif action == "N":
        position = (position[0], position[1] + value)
    elif action == "S":
        position = (position[0], position[1] - value)
    elif action == "E":
        position = (position[0] + value, position[1])
    elif action == "W":
        position = (position[0] - value, position[1])
    elif action == "R":
        facing = (facing + value) % 360
    elif action == "L":
        facing = (facing - value) % 360
print(position, abs(position[0]) + abs(position[1]))
