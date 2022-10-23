# 출력 잘되는데 틀렸대
# ^^ 싯

n = int(input())
ratio = 0
r = 0

if( n == 1):
    print("1")
else:
    while True:
        if (n < 7 + ratio):
            print(r + 2)
            break
        else:
            r += 1
            ratio += 6 * r + 6