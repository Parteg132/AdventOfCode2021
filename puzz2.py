#puzzle 2 part 2

def main():
    f = open("input2.txt", "r")

    x = 0
    y = 0
    aim = 0

    for i in f:
        i = i.rstrip()
        if i[0] == 'f':
            x += int(i[-1])
            y += int(i[-1]) * aim
        elif i[0] == 'u':
            aim -= int(i[-1])
        elif i[0] == 'd':
            aim += int(i[-1])

    print("Answer:", x*y)

    f.close()

if __name__ == "__main__":
    main()