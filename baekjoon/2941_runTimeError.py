 # 런타임 오류
a1 = input()
a2 = list(a1)
cnt = len(a2)


for i in range(len(a2)):
    if (a2[i] == "=") or (a2[i] == "-"):
        cnt -= 1
    if ((a2[i] == "l") or (a2[i] == "n")) and (a2[i + 1] == "j"):
        cnt -= 1
    if (a2[i] == "d") and (a2[i + 1] == "z") and (a2[i + 2] == "="):
        cnt -= 1

print(cnt)