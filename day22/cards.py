with open("input.txt") as f:
    players = f.read().split("\n\n")
    player1, player2 = map(lambda x: [int(i) for i in x.split("\n")[1:]], players)


def calculate_score(player1, player2):
    winner = player1 if len(player1) > 0 else player2
    winner.reverse()
    score = 0
    for i, card in enumerate(winner):
        score += (i + 1) * card
    return score


def part1(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1 += [card1, card2]
        elif card2 > card1:
            player2 += [card2, card1]

    print(calculate_score(player1, player2))


part1(player1[:], player2[:])


def calculate_state(player1):
    return "p1:" + ",".join([str(i) for i in player1])


def part2(player1, player2, game):
    # print("=== Game %s ===" % game)
    states = []
    round = 1
    while len(player1) > 0 and len(player2) > 0:
        # print("--- Round %s (game %s) ---" % (round, game))
        state = calculate_state(player1)
        if state in states:
            # print("Found previous state, player1 wins round %s of game %s" % (round, game))
            return player1, player2
        else:
            # print("new configuration %s" % state)
            states.append(state)
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            # print("Player1 plays %s" % card1)
            # print("Player2 plays %s" % card2)
            if len(player1) >= card1 and len(player2) >= card2:
                # print("play another round with %s and %s" % (player1[:card1], player2[:card2]))
                p1, p2 = part2(player1[:card1], player2[:card2], game + 1)
                if len(p1) > 0:
                    # print("The winner of game %s is player 1!" % (game + 1))
                    player1 += [card1, card2]
                else:
                    # print("The winner of game %s is player 2!" % (game + 1))
                    player2 += [card2, card1]
            else:
                if card1 > card2:
                    # print("player1 wins round %s of game %s" % (round, game))
                    player1 += [card1, card2]
                else:
                    # print("player2 wins round %s of game %s" % (round, game))
                    player2 += [card2, card1]
        round += 1
    if game == 1:
        print(calculate_score(player1, player2))
    else:
        return player1, player2


part2(player1[:], player2[:], 1)
