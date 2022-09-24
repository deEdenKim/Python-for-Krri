# 영수증 계산 총 가격
receiptTotal = int(input())

# 종류 개수
category = int(input())

#실제 총 가격
realTotal = 0

# 종류 개수만큼 반복문 
for i in range(category):
#   input: 가격, 개수
    price, num = map(int, input().split())
    realTotal += (price * num)
    
# total이 0이라면 Yes, 아니면 No
if realTotal == receiptTotal:
    print("Yes")
else:
    print("No")