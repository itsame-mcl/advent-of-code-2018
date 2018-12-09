from blist import blist

players = 427
last_marble = 7072300

scores = [0] * players
marbles = blist([0])
insert = marbles.insert

current_marble = 0
current_player = 0

for marble in range(1,last_marble + 1):
    nb_marbles = len(marbles)
    if marble % 23 == 0:
        var_score = marble
        current_marble = (current_marble + nb_marbles - 7) % nb_marbles
        var_score = var_score + marbles[current_marble]
        del marbles[current_marble]
        scores[current_player] = scores[current_player] + var_score
    else:
        current_marble = (current_marble + 2) % nb_marbles
        insert(current_marble, marble)       
    current_player = (current_player + 1) % players

print(max(score for score in scores))