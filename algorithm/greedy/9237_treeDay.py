import sys
input = sys.stdin.readline

n = int(input())
treeList = list(map(int, input().split()))

treeList.sort(reverse=True)
result=0
day=1
for i in range(len(treeList)):
    com = day+treeList[i]
    result=max(result, com)
    day+=1

print(result+1)