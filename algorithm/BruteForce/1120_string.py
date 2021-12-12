import sys
input = sys.stdin.readline

strA, strB = input().split()
answer=50


for i in range(len(strB)-len(strA)+1):
    count=0
    for j in range(len(strA)):
        if strA[j]!=strB[i+j]:
            count+=1

    if answer>count:
        answer=count
print(answer)
    






"""
AAA BBBBB 이렇게 있다고 생각 할 때
문자열 비교를

BBBBB   BBBBB   BBBBB
AAA      AAA      AAA

이렇게 비교해서 최소 카운트를 구함

두 문자열 차이를 이용해서 반복시키는것도 활용
"""