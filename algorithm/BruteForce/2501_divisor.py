import sys
input = sys.stdin.readline

n, k = map(int, input().split())

tempList=[]
for i in range(1, n+1):
    if n%i==0:
        tempList.append(i)

    if len(tempList)==k:
        print(tempList[k-1])
        break
else:
    print(0)