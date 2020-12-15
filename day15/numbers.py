with open("input.txt") as f:
    numbers = f.readline().split(",")

turns = {}
for i, number in enumerate(numbers):
    turns[int(number)] = [i + 1]
turn = len(numbers) + 1
number = int(numbers[-1])
while turn <= 2020:
    if number in turns.keys() and len(turns[number]) > 1:
        number = turns[number][-1] - turns[number].pop(0)
        turns[number] = turns.get(number, []) + [turn]
    else:
        turns[number] = [turn - 1]
        number = 0
        turns[number] = turns[number] + [turn]
    turn += 1
print(number)


