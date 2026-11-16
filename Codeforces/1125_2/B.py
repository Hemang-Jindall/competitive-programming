t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    stack = []
    printed = set()

    for i in range(n):
        doc = i + 1

        if s[i] == '1':
            stack.append(doc)

        elif s[i] == '2':
            if stack:
                printed.add(stack.pop())
            else:
                printed.add(doc)

        else:  # command 3
            printed.add(doc)

    ans = [i for i in range(1, n + 1) if i not in printed]

    print(len(ans))
    print(*ans)