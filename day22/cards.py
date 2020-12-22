with open("input.txt") as f:
    players = f.read().split("\n\n")
    player1, player2 = map(lambda x: x.split("\n")[1:], players)

while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if int(card1) > int(card2):
        player1 += [card1, card2]
    elif int(card2) > int(card1):
        player2 += [card2, card1]

winner = player1 if len(player1) > 0 else player2
winner.reverse()
score = 0
for i, card in enumerate(winner):
    score += (i + 1) * int(card)
print(score)
