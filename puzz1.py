#puzzle 1 part 2

def counting(tab):
    count = 0
    a = 0
    b = 0
    temp = 0
    for i in range(1, len(tab)):

        if i <= 3:
            a += tab[i-1]
        else:
            a -= tab[i-4]
            a += tab[i-1]
    
        if i < 4:
            b += tab[i]
        elif i >= 4:
            b -= tab[i-3]
            b += tab[i]

        if b > a and i >= 3:
            count += 1

    return count

def main():
    tab = []

    with open("input.txt", 'r') as f:
        for line in f.readlines():
            tab.append(int(line.rstrip()))

    print("count =", counting(tab))

if __name__ == "__main__":
    main()