players = 427
last_marble = 70723

scores = [0] * players
marbles = [0]
current_marble = 0
current_player = 0
for marble in range(1,last_marble + 1):
    if marble % 23 != 0:
        current_marble += 2
        if current_marble > len(marbles):
            current_marble -= len(marbles)
        if current_marble < len(marbles):
            marbles.insert(current_marble, marble)
        elif current_marble == len(marbles):
            marbles.append(marble)
    else:
        scores[current_player] += marble
        current_marble -= 7
        if current_marble < 0:
            current_marble += len(marbles)
        scores[current_player] += marbles[current_marble]
        del marbles[current_marble]
    current_player += 1
    if current_player == players:
        current_player = 0

print(max(score for score in scores))