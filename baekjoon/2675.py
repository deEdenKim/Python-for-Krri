# 서현.ver
# num = int(input())

# for i in range(num):
#     r, p = map(input().split())
#     int(r)
#     for j in range(r):
#         k = 0
#         print(p[k])
#         k += 1


num = int(input())

for i in range(num):
    r, p = input().split()
    text = ''
    # 단어 자릿수만큼 반복
    # 파이썬은 문자열로 반복문을 쓸 수 있다. 0번째 자리부터 r번씩 반복하여 출력한다
    for j in p: 
        text += j * int(r)
    
    print(text)
    
    
