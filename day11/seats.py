data = {}

with open("input.txt") as f:
    y = 0
    for _y in [line.rstrip() for line in f]:
        x = 0
        for _x in _y:
            data[(y, x)] = _x
            x += 1
        y += 1
directions = [(-1, -1), (-1, 0), (1, 0), (1, -1), (0, -1), (0, 1), (1, 1), (-1, 1)]


def adjacent_occupied(point, grid):
    adjacent_points = [(point[0] + y, point[1] + x) for y, x in directions]
    return len([p for p in adjacent_points if grid.get(p, '.') == '#'])


def part1(g):
    grid = dict(g)
    while True:
        adjacent = {k: adjacent_occupied(k, grid) for k in grid.keys()}
        new_grid = grid.copy()
        for point in grid.keys():
            if grid[point] == '#' and adjacent[point] >= 4:
                grid[point] = 'L'
            elif grid[point] == 'L' and adjacent[point] == 0:
                grid[point] = '#'
        if new_grid == grid:
            return sum(value == "#" for value in grid.values())


print(part1(data))


def visible_occupied(point, grid):
    visible = 0
    for y, x in directions:
        dy, dx = point[0] + y, point[1] + x
        while (dy, dx) in grid.keys():
            if grid[(dy, dx)] != '.':
                visible += 1 if grid[(dy, dx)] == '#' else 0
                break
            dy += y
            dx += x
    return visible


def part2(g):
    grid = dict(g)
    while True:
        visible = {k: visible_occupied(k, grid) for k in grid.keys()}
        new_grid = grid.copy()
        for point in new_grid.keys():
            if new_grid[point] == '#' and visible[point] >= 5:
                new_grid[point] = 'L'
            elif new_grid[point] == 'L' and visible[point] == 0:
                new_grid[point] = '#'
        if new_grid == grid:
            return sum(value == '#' for value in grid.values())
        grid = new_grid


print(part2(data))
