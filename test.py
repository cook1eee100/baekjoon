import sys
from collections import deque
input = sys.stdin.readline



test=10
a=[[1,4,5,8,10,13,16,19], [2,4,67,9,0, 8, 23, 13]]


for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j])
        # if a[i][j]==10:
            
        #     break

    else:
        print("작업됨")
        continue
    break