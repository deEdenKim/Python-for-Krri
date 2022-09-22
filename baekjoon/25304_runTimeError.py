#runTime error
# # 총 가격
total = int(input())

# 종류 개수
category = int(input())

# 종류 개수만큼 반복문 
for i in range(category):
#   input: 가격, 개수
    price = int(input())
    num = int(input())
#   a = (총 가격) - (input한 가격 * 개수)
    total -= (price * num)
    
# total이 0이라면 Yes, 아니면 No
if total == 0:
    print("Yes")
else:
    print("No")