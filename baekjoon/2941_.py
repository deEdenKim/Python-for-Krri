# https://codingpractices.tistory.com/entry/%EB%B0%B1%EC%A4%80-2941%EB%B2%88-%ED%81%AC%EB%A1%9C%EC%95%84%ED%8B%B0%EC%95%84-%EC%95%8C%ED%8C%8C%EB%B2%B3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
a1 = input()
a2 = len(a1)
idx = 0
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro:
    cnt = a1.count(i)
    a2 -= cnt * len(i)
    idx += 1 * cnt
    a1 = a1.replace(i, " ")

print(a2 + idx)