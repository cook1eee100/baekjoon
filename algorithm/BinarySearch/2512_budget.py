import sys
input=sys.stdin.readline

n=int(input())
graph=list(map(int, input().split()))
m=int(input())

start=1
end=max(graph)
answer=0
while start<=end:
    mid = (start+end)//2

    totalBudget=0
    for i in graph:
        if i>=mid:
            totalBudget+=mid
        else:
            totalBudget+=i

    if totalBudget > m:
        end=mid-1

    elif totalBudget <= m:
        answer=mid
        start=mid+1

print(answer)