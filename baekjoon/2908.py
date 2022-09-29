num1, num2 = input().split()
#원래 num1, num2 = int(input().split())으로 썼는데 런타임에러가 나왔다
#아래 reverse 변수에 저장할 때 두번 int가 들어가서 그런가..?

#reverse1 = (num1//100) + (((num1 % 100) // 10) * 10) + ((num1 % 10) * 100)
#reverse2 = (num2//100) + (((num2 % 100) // 10) * 10) + ((num2 % 10) * 100)

reverse1 = int(str(num1)[::-1])
reverse2 = int(str(num2)[::-1])

if reverse1 < reverse2:
    print(reverse2)

elif reverse1 > reverse2:
    print(reverse1)