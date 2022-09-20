#입력한 수를 리스트에 넣고 정해진 말의 수로 빼는 방법


#정해진 말의 수
chess = [1, 1, 2, 2, 2, 8] 

#input을 리스트로 바꾸는 과정
#   1. split: input값을 전부 한 자리로 쪼갠다
#   2. 뜻: input값을 쪼개서 int형식으로 a릐스트를 생성하라
a = list(map(int, input().split()))

#
for i in range(6):
    print(chess[i]-a[i], end=' ')