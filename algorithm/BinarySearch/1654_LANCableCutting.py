import sys
input = sys.stdin.readline

k, n = map(int, input().split())
LANList=[]
for i in range(k):
    LANList.append(int(input()))

start=1
end=max(LANList)
while start<=end:
    mid=(start+end)//2
    
    count=0
    for i in LANList:
        count+=i//mid
    
    if count >= n:
        start=mid+1
    else:
        end=mid-1

print(end)
