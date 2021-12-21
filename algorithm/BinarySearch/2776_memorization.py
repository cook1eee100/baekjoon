"""
import sys
input = sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    nList=list(map(int, input().split()))
    nList.sort()
    m=int(input())
    mList=list(map(int, input().split()))

    for num in mList:
        start=0
        end=n-1
        while start<=end:
            mid =(start+end)//2

            if num ==nList[mid]:
                print(1)
                break

            elif num>nList[mid]:
                start=mid+1
            else:
                end=mid-1

        else:
            print(0)
"""

import sys
input = sys.stdin.readline

t= int(input())

for _ in range(t):
    n=int(input())
    nList=set(map(int, input().split()))
    m=int(input())
    mList=list(map(int, input().split()))

    for num in mList:
        if num in nList:
            print(1)
        else:
            print(0)