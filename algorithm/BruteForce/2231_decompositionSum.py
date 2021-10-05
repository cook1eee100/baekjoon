import sys
input = sys.stdin.readline

n = int(input())

answer=0
for i in range(1, n-1):
    temp = list(map(int, str(i)))
    if i+sum(temp)==n:
        answer=i
        break


print(answer)




"""
숫자를 str로 감싸서 문자열로 만들고 list()를 씌워 리스트로 변환
for _ in a:     a가 문자열 가능
"""