from functools import cache
from itertools import product

# positions... 0-9, score = position + 1


@cache
def play_round(p1_score, p1_pos, p2_score, p2_pos, turn):
    wins = [0, 0]

    for rolls in product(range(1, 4), range(1, 4), range(1, 4)):
        step = sum(rolls)
        p_score, p_pos = (p1_score, p1_pos) if turn == 0 else (p2_score,
                                                               p2_pos)
        p_pos = (p_pos + step) % 10
        p_score += p_pos + 1
        if p_score >= 21:
            if turn == 0:
                wins[0] += 1
            else:
                wins[1] += 1
        else:
            if turn == 0:
                wins_0, wins_1 = play_round(p_score, p_pos, p2_score, p2_pos,
                                            1)
            else:
                wins_0, wins_1 = play_round(p1_score, p1_pos, p_score, p_pos,
                                            0)
            wins[0] += wins_0
            wins[1] += wins_1
    return wins


print(play_round(0, 5, 0, 3, 0))
