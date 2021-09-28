import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    fiboList=[[1,0], [0,1]]

    for i in range(2, n+1):
        fiboList.append([fiboList[i-1][0]+fiboList[i-2][0], fiboList[i-1][1]+fiboList[i-2][1]])
    print(fiboList[n][0], fiboList[n][1])






"""
[0의 개수, 1의 개수]   f(n)= f(n-1)+f(n-2)
[1,0], [0,1], [1,1], [1,2], [2,3], [3,5]
"""