t = int(input())

vowels = "aeiou"

for _ in range(t):
    n = int(input())

    base = n // 5
    extra = n % 5

    ans = ""

    for i in range(5):
        count = base

        if i < extra:
            count += 1

        ans += vowels[i] * count

    print(ans)