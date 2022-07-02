#part 1 + 2
import re

def part2(data, diagram):
    count = 0

    for i in range(4, len(data)+1, 4):
        x1 = int(data[i-4])
        x2 = int(data[i-2])
        y1 = int(data[i-3])
        y2 = int(data[i-1])
        deltaX = x2 - x1
        deltaY = y2 - y1
        if x1 == x2:
            if y1 < y2:
                for j in range(y1, y2+1, 1):
                    diagram[j][x1] += 1
                    if diagram[j][x1] == 2:
                        count += 1
            else:
                for j in range(y2, y1+1, 1):
                    diagram[j][x1] += 1
                    if diagram[j][x1] == 2:
                        count += 1
        elif y2 == y1:
            if x1 < x2:
                for j in range(x1, x2+1, 1):
                    diagram[y1][j] += 1
                    if diagram[y1][j] == 2:
                        count += 1
            else:
                for j in range(x2, x1+1, 1):
                    diagram[y1][j] += 1
                    if diagram[y1][j] == 2:
                        count += 1
        elif abs(deltaX) == abs(deltaY):
            if x1 < x2 and y1 < y2:
                for i, j in zip(range(x1, x2+1, 1), range(y1, y2+1, 1)):
                    diagram[j][i] += 1
                    if diagram[j][i] == 2:
                        count += 1
            elif x1 > x2 and y1 > y2:
                for i, j in zip(range(x2, x1+1, 1), range(y2, y1+1, 1)):
                    diagram[j][i] += 1
                    if diagram[j][i] == 2:
                        count += 1
            elif x1 < x2 and y1 > y2:
                if (deltaX < 0 and deltaY < 0) or (deltaX > 0 and deltaY > 0):
                    for i, j in zip(range(x1, x2+1, 1), range(y2, y1+1, 1)):
                        diagram[j][i] += 1
                        if diagram[j][i] == 2:
                            count += 1
                else:
                    for i, j in zip(range(x2, x1-1, -1), range(y2, y1+1, 1)):
                        diagram[j][i] += 1
                        if diagram[j][i] == 2:
                            count += 1
            elif x1 > x2 and y1 < y2:
                if (deltaX < 0 and deltaY < 0) or (deltaX > 0 and deltaY > 0):
                    for i, j in zip(range(x2, x1+1, 1), range(y1, y2+1, 1)):
                        diagram[j][i] += 1
                        if diagram[j][i] == 2:
                            count += 1
                else:
                    for i, j in zip(range(x1, x2-1, -1), range(y1, y2+1, 1)):
                        diagram[j][i] += 1
                        if diagram[j][i] == 2:
                            count += 1
    return count

def main():
    data = []

    with open("input5.txt") as input:
        input = open('input5.txt').read()
        lines = [[int(i) for i in re.split(r'\W+', line)] for line in input.strip().splitlines()]

    for a in range(len(lines)):
        for b in range(len(lines[0])):
            data.append(lines[a][b])
        
    diagram = [[0 for _ in range(max(data)+1)] for _ in range(max(data)+1)]

    #for i in range(len(diagram)):
    #    print(diagram[i])
    #    print()

    print("Part 2 answer:", part2(data, diagram))

if __name__ == "__main__":
    main()