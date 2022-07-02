import statistics as s

def part1(horizontal):
    m = s.median(horizontal)
    totalFuel = 0

    for i in horizontal:
        totalFuel += abs(i - m)
    
    return totalFuel

def part2(horizontal):
    m = round(s.mean(horizontal), 0)

    totalFuel = [0, 0, 0, 0, 0]
    b = -2

    for a in range(5):
        for i in horizontal:
            for j in range(1, int(abs(i - m + b))+1):
                totalFuel[a] += j
        b += 1
    return min(totalFuel)

def main():
    horizontal = []

    with open("input7.txt", "r") as f:
        lines = f.readline().split(",")
        horizontal = list(map(int, lines))

    print("Part1:", part1(horizontal))
    print("Part2:", part2(horizontal))

if __name__ == "__main__":
    main()