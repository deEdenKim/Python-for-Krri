# 이외 알파벳 카운트 방법 오류
a1 = input()
a2 = list(a1)
cnt = 0


for i in range(len(a2)):
    if (a2[i] == "c") and (a2[i + 1] == "="):
        cnt += 1
    elif (a2[i] == "c") and (a2[i + 1] == "-"):
        cnt += 1
    elif (a2[i] == "d") and (a2[i + 1] =="z") and (a2[i + 2] == "="):
        cnt +=1
    elif (a2[i] == "d") and (a2[i + 1] == "-"):
        cnt += 1
    elif (a2[i] == "l") and (a2[i + 1] == "j"):
        cnt += 1
    elif (a2[i] == "n") and (a2[i + 1] == "j"):
        cnt += 1
    elif (a2[i] == "s") and (a2[i + 1] == "="):
        cnt += 1
    elif (a2[i] == "z") and (a2[i + 1] == "="):
        cnt += 1
    #  elif (a2[i] == "a") and (a2[i] == "b") and (a2[i] == "e") and (a2[i] == "f") and  (a2[i] == "g") and (a2[i] == "h") and (a2[i] == "i") and (a2[i] == "j") and (a2[i] == "k") and (a2[i] == "m") and (a2[i] == "o") and (a2[i] == "p") and (a2[i] == "q") and (a2[i] == "r") and (a2[i] == "t") and (a2[i] == "u") and (a2[i] == "v") and (a2[i] == "w") and (a2[i] == "x") and(a2[i] == "y"):
    #     cnt += 1
print(cnt)