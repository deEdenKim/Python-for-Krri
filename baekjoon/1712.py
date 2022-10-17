a, b, c = map(int, input().split())


if c <= b:
    print(-1)
else:
    n = a / (c - b)
    print(int(n) + 1)