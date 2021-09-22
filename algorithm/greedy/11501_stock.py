import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    dayList=list(map(int, input().split()))
    
    answer=0
    mx=dayList[-1]
    for i in range(n-2, -1, -1):
        if dayList[i] > mx:
            mx = dayList[i]
        else:
            answer+= mx-dayList[i]

    print(answer)