positions = [10, 7]
scores = [0, 0]

die = 1
rolls = 0
player = 0

while max(scores) < 1000:

    move = 0
    for _ in range(3):
        move += die
        die += 1
        if die == 1001:
            die = 1
        rolls += 1
    positions[player] += (move % 10)
    if positions[player] > 10:
        positions[player] -= 10
    scores[player] += positions[player]
    
    player = 1-player

print("part one: ", min(scores)*rolls)


wins = [0, 0]
states = {}
states[((10, 7), (0, 0), 0)] = 1

def roll(s, n):
    pos, sc, p = s

    for d_1 in [1, 2, 3]:
        for d_2 in [1, 2, 3]:
            for d_3 in [1, 2, 3]:
                new_p = [x for x in pos]
                new_s = [x for x in sc]

                new_p[p] += (d_1+d_2+d_3)
                if new_p[p] > 10:
                    new_p[p] -= 10
                
                new_s[p] += new_p[p]
                if new_s[p] >= 21:
                    wins[p] += n
                else:
                    new_p = tuple(new_p)
                    new_s = tuple(new_s)
                    if (new_p, new_s, 1-p) in states:
                        states[(new_p, new_s, 1-p)] += n
                    else:
                        states[(new_p, new_s, 1-p)] = n

while len(states) > 0:
    for st in states:
        break
    v = states.pop(st)
    roll(st, v)

print("part two: ", max(wins))
