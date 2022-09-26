word = input()
alphabet = list(range(97,123)) # a - z 아스키 코드

# baekjoon을 입력했을 때, [b,a,e,k,j,o,o,n]으로 입력된다
# a부터 find함수를 이용하여 찾는데, find 함수는 발견된 위치의 인덱스 값을 출력한다

for i in alphabet:
    print(word.find(chr(i))) 