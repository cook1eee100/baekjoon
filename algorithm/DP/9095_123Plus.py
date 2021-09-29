import sys
input = sys.stdin.readline

t=int(input())
dpList=[0,1,2,4]
for _ in range(t):
    n=int(input())

    if len(dpList)<n+1:
        for i in range(4, n+1):
            if len(dpList) <i+1:
                dpList.append(dpList[i-1]+dpList[i-2]+dpList[i-3])
    print(dpList[n])


"""
1 1     1
2 2     11 2
3 4     111 12 21 3
4 7     1111 112 121 211 22 13 31
5 13    .......
"""