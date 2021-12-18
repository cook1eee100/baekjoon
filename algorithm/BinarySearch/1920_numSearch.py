import sys
input = sys.stdin.readline

n = int(input())
nList = list(map(int, input().split()))
nList.sort()
m = int(input())
mList = list(map(int, input().split()))


for num in mList:
    start=0
    end=len(nList)-1

    while start<=end:
        mid = (start+end)//2
        if num==nList[mid]:
            print(1)
            break
        elif num>nList[mid]:
            start=mid+1

        else:
            end=mid-1

    else:
        print(0)