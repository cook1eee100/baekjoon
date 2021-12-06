n = int(input())
aList=list(map(int, input().split()))
bList=list(map(int, input().split()))

aList.sort()
bList.sort(reverse=True)

total=0
for i in range(n):
    total+=aList[i]*bList[i]

print(total)
