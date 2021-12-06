# 길이 잴 때
import sys
from typing import Sequence
input = sys.stdin.readline

n = int(input())
sequenceList = list(map(int, input().split()))

dpList=[1 for _ in range(n)]


for i in range(1, n):
    maxValue=0
    idx=i
    for j in range(i-1, -1, -1):
        if maxValue < sequenceList[j] < sequenceList[i]:
            maxValue=sequenceList[j]
            idx=j
    dpList[i]=dpList[idx]+1
    print(dpList)
print(dpList)



# import sys
# from typing import Sequence
# input = sys.stdin.readline

# n = int(input())
# sequenceList = list(map(int, input().split()))

# dpList=[[0]]

# for i in range(1, n):
#     for j in range(i-1, -1, -1):
#         if sequenceList[i]>sequenceList[j]:
#             dpList.append(dpList[j]+[i])
#             break

# print(dpList)

# 1 2 3 6 7 5 8
# 1 2 3 4 5 4 6