#Doesn't work
#solved on hand - in the input

from functools import lru_cache
import sys 
import random
sys.setrecursionlimit(3000)
# data = []
# expense = {"A": 1, "X": 1, "B": 10, "Y": 10, "C": 100, "Z": 100, "D": 1000, "W": 1000,}
# slotted = [False for _ in range(8)]
price = [1, 10, 100, 1000]
type = "ABCD"
# positions = ((9, 3), (7, 3), (9, 2), (3, 2), (7, 2), (5, 2), (5, 3), (3, 3))
positions = (
    (7, 4), (7, 5), (9, 3), (9, 5),
    (3, 2), (5, 4), (7, 3), (9, 2),
    (5, 2), (5, 3), (7, 2), (9, 4),
    (3, 3), (3, 4), (3, 5), (5, 5),
    )
ind = [i for i in range(16)]
# positions = ((9, 3), (7, 3), (10, 1), (3, 2), (7, 2), (5, 2), (5, 3), (3, 3))
# result = 0

# @lru_cache(maxsize=None)
def move(data):
    i, pos = data
    home = 3 + (i // 4) * 2
    curr = pos[i][0]

    if pos[i][1] == 1:
        if curr > home:
            for t in range(home, curr):
                if (t, 1) in pos:
                    return ()
        else:
            for t in range(curr+1, home):
                if (t, 1) in pos:
                    return ()

        if ((home, 5) not in pos):
            return (
                (
                    (home, 5), 
                    (abs(home-curr) + 4)*price[i//4]
                ),
            )
        elif ((home, 4) not in pos) and (pos.index((home, 5))//4 == i//4):
            return (
                (
                    (home, 4), 
                    (abs(home-curr) + 3)*price[i//4]
                ),
            )
        elif ((home, 4) not in pos):
            return ()
        elif ((home, 3) not in pos) and (pos.index((home, 4))//4 == i//4) and (pos.index((home, 5))//4 == i//4):
            return (
                (
                    (home, 3), 
                    (abs(home-curr) + 2)*price[i//4]
                ),
            )
        elif ((home, 3) not in pos):
            return ()
        elif ((home, 2) not in pos) and (pos.index((home, 4))//4 == i//4) and (pos.index((home, 5))//4 == i//4) and (pos.index((home, 3))//4 == i//4):
            return (
                (
                    (home, 2), 
                    (abs(home-curr) + 1)*price[i//4]
                ),
            )
        else:
            return ()
    
    elif pos[i][1] == 3 and ((pos[i][0], 2) in pos):
        # print(i, "a-asd-asd-asd-")
        return ()
    elif pos[i][1] == 4 and ((pos[i][0], 3) in pos):
        # print(i, "----------")
        return ()
    elif pos[i][1] == 5 and ((pos[i][0], 4) in pos):
        # print(i, "++++++++")
        return ()
    
    elif pos[i][0] == home:
        correct = True
        for dep in range(pos[i][1]+1, 6):
            if not (pos.index((curr, dep))//4 == i//4):
                correct = False
        if correct:
            return ()


    available = []
    for x in range(curr, 12):
        if (x, 1) in pos:
            break
        if x not in [3, 5, 7, 9]:
            available.append(
                (
                    (x, 1),
                    (x-curr + pos[i][1]-1)*price[i//4]
                )
            )
    for x in range(curr, 0, -1):
        if (x, 1) in pos:
            break
        if x not in [3, 5, 7, 9]:
            available.append(
                (
                    (x, 1),
                    (curr-x + pos[i][1]-1)*price[i//4]
                )
            )
    return tuple(available)

@lru_cache(maxsize=None)
def solution(pos):
    # print(pos)

    fst = [x[0] for x in pos]
    snd = [x[1] for x in pos]
    if (min(snd) >= 2) and (fst == sorted(fst)):
        print("HEEEEREEEEEEEE")
        return 0
    

    best = 10000000

    # random.shuffle(ind)
    for i in ind:
        av = move((i, pos))
        if av == ():
            continue
        for (t, p) in av:
            
            # print(pos, i)
            # print(av, t, p)
            pos = list(pos)
            pos[i] = t
            pos = tuple(pos)
            # print(pos, i)
            # print(pos, i)

            this_one = solution(pos) + p
            if this_one < best:
                best = this_one

    return best

case = (
    (3, 5), (2, 1), (1, 1), (9, 5),
    (3, 2), (5, 5), (10, 1), (8, 1),
    (7, 4), (7, 3), (7, 5), (9, 4),
    (3, 3), (3, 4), (4, 1), (11, 1),
    )

p = 1000*8 + 100*12 + 10 * 16 + 18
tog = [32808]
for aaa in range(16):
    print(aaa//4, move((aaa, case)))
print(solution(positions), p)