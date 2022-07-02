def part1(tab1, tab_zeros, tab_ones):
    gamma_rate = []
    epsilon_rate = []

    for i in range(len(tab1[0])):
        for j in tab1:
            if int(j[i]) == 0:
                tab_zeros.append(0)
            else:
                tab_ones.append(1)

        if len(tab_zeros) > len(tab_ones):
            gamma_rate.append(0)
            epsilon_rate.append(1)
        else:
            gamma_rate.append(1)
            epsilon_rate.append(0)

        tab_zeros.clear()
        tab_ones.clear()
    return gamma_rate, epsilon_rate

def part2(tab1, tab_zeros, tab_ones):
    tab2 = tab1[:]
    tab3 = tab1[:]

    for i in range(len(tab2[0])):
        for j in tab2:
            if int(j[i]) == 0:
                tab_zeros.append(j)
            else:
                tab_ones.append(j)

        if len(tab2) == 1:
            break
        elif len(tab_zeros) > len(tab_ones):
            tab2 = tab_zeros[:]
        else:
            tab2 = tab_ones[:]

        tab_zeros.clear()
        tab_ones.clear()

    for i in range(len(tab3[0])):
        for j in tab3:
            if int(j[i]) == 0:
                tab_zeros.append(j)
            else:
                tab_ones.append(j)

        if len(tab3) == 1:
            break
        elif len(tab_zeros) > len(tab_ones):
            tab3 = tab_ones[:]
        else:
            tab3 = tab_zeros[:]

        tab_zeros.clear()
        tab_ones.clear()

    return tab2, tab3


def main():
    with open("input3.txt") as f:
        tab1 = f.readlines()

    tab1 = list(map(str.rstrip, tab1))
    tab_zeros = []
    tab_ones = []

    g, e = part1(tab1, tab_zeros, tab_ones)
    dG = int(''.join(str(el) for el in g), 2)
    dE = int(''.join(str(el) for el in e), 2)

    t2, t3 = part2(tab1, tab_zeros, tab_ones)
    dO = int(t2[0], 2)
    dC02 = int(t3[0], 2)
    print("Answer to part 1:", dG * dE)
    print("Answer to part 2:", dO * dC02)

if __name__ == "__main__":
    main()