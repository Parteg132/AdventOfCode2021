def check_horizontal(players, counting):
    for row in range(len(players)):
        bingo = True
        for col in range(len(players[row])):
            if counting[row][col] == 0:
                    bingo = False
                    break
        if bingo == True:
            sum = 0
            for m in range(len(players)):
                for n in range(len(players[m])):
                    if counting[m][n] == 0:
                        sum += int(players[m][n])
                    else:
                        continue
            return sum
    return 0

def check_vertical(players, counting):
    for row in range(len(players)):
        bingo = True
        for col in range(len(players[row])):
            if counting[col][row] == 0:
                    bingo = False
                    break
        if bingo == True:
            sum = 0
            for m in range(len(players)):
                for n in range(len(players[m])):
                    if counting[m][n] == 0:
                        sum += int(players[m][n])
                    else:
                        continue
            return sum
    return 0

def main():
    print(""" |
 |
\/ Answer to part 1 is the 1st Puzzle answer""")
    with open("input4.txt") as f:
        tab1 = f.readline().rstrip().split(",")
        lines = [line.split() for line in f if line.strip()]
        counting = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(int(len(lines)/5))]

    players = []
    i = 0
    j = 5

    for x in range(int(len(lines)/5)):
        players.append(lines[i:j])
        i += 5
        j += 5
    sth = 0
    for x in tab1:
        for a in range(len(players)):
            for b in range(5):
                for c in range(5):
                    if players[a][b][c] == x:
                        counting[a][b][c] = 1
        isResult = False
        for i in range(len(players)):
            result = check_horizontal(players[i], counting[i])
            if result != 0:
                for d in range(5):
                    for e in range(5):
                        players[i][d][e] = int(players[i][d][e]) + 100
                        counting[i][d][e] = 0
                isResult = True
                sth += 1
                print("Number that was just called:", int(x))
                print("Result:", result)
                print("Puzzle answer:", int(x) * result)
                if sth == int(len(lines)/5):
                    break
            result = check_vertical(players[i], counting[i])
            if result != 0:
                for d in range(5):
                    for e in range(5):
                        players[i][d][e] = int(players[i][d][e]) + 100
                        counting[i][d][e] = 0
                isResult = True
                sth += 1
                print("Number that was just called:", int(x))
                print("Result:", result)
                print("Puzzle answer:", int(x) * result)
                if sth == int(len(lines)/5):
                    break
        if isResult:
            if sth == len(players):
                print("^^^ Answer to part 2")
                break


if __name__ == "__main__":
    main()