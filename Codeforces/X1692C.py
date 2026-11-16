t = int(input())

for _ in range(t):
    input()  # consume the empty line

    g = [input() for _ in range(8)]

    for i in range(1, 7):
        for j in range(1, 7):
            if (
                g[i][j] == '#'
                and g[i - 1][j - 1] == '#'
                and g[i - 1][j + 1] == '#'
                and g[i + 1][j - 1] == '#'
                and g[i + 1][j + 1] == '#'
            ):
                print(i + 1, j + 1)
                break
        else:
            continue
        break