players = []
numbers = list(map(int, input().split(","))) 
input()

while True:
    try:
        board = []
        for _ in range(5):
            line = list(map(int, input().split()))
            board.append(line)
        players.append(board)
        input()

    except:
        break



def check(b, i, j):
    #row
    if sum(b[j]) == -5:
        return True

    #column
    if sum([b[k][i] for k in range(5)]) == -5:
        return True

    #nothing found    
    return False


def value(b):
    return sum([sum([b[j][i] for i in range(5) if b[j][i] > 0]) for j in range(5)])


winners = set()
def play(loc, x):
    b = players[loc]
    for j in range(5):
        for i in range(5):
            if b[j][i] == x:
                b[j][i] = -1
                
                if check(b, i, j):
                    if loc not in winners:
                        print("bingo")
                        print(value(b) * x)
                        winners.add(loc)
                        return 1
                else:
                    return -1

end = False
for n in numbers:
    for i in range(len(players)):
        x = play(i, n)
        # in the 1st part, end after the first BINGO
        # if x == 1:
        #     end = True
        #     break
