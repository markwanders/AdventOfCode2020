grid = {}

with open("input.txt") as f:
    y = 0
    for _y in [line.rstrip() for line in f]:
        x = 0
        for _x in _y:
            grid[(y, x)] = _x
            x += 1
        y += 1


def adjacent_occupied(point, grid):
    adjacent_points = [(y, x) for y in range(point[0] - 1, point[0] + 2) for x in range(point[1] - 1, point[1] + 2)]
    return len([p for p in adjacent_points if grid.get(p, '.') == '#' and p != point])


seen = set()
while True:
    occupied = sum(value == "#" for value in grid.values())
    if occupied in seen:
        print(occupied)
        break
    seen.add(occupied)
    adjacent = {k: adjacent_occupied(k, grid) for k in grid.keys()}
    for point in grid.keys():
        if grid[point] == '#' and adjacent[point] >= 4:
            grid[point] = 'L'
        elif grid[point] == 'L' and adjacent[point] == 0:
            grid[point] = '#'
