import sys
input = sys.stdin.readline

t=int(input())
dpList=[0, 1, 1]

for _ in range(t):
    n=int(input())
    if len(dpList)<n+1:
        for i in range(len(dpList), n+1):
            dpList.append(dpList[i-3]+dpList[i-2])
    print(dpList[n])


"""
파도반 수열 검색
점화식은 P(n)=P(n-3)+P(n-2)
P(0)부터 [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, ...]
"""