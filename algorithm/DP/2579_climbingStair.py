import sys
input = sys.stdin.readline

n=int(input())
stairList=[0]
for i in range(n):
    stairList.append(int(input()))

dpList=[0]
for i in range(1, n+1):
    if i==1:
        dpList.append(stairList[i])
    elif i==2:
        dpList.append(stairList[i]+stairList[i-1])
    else:
        dpList.append(max(dpList[i-3]+stairList[i-1]+stairList[i], dpList[i-2]+stairList[i]))
print(dpList[n])



"""
해당층까지 더해서 최대가 되는 경우
해당층까지 올라올수 잇는 경우
1) 현재-2 칸에서 현재-1 칸 뛰고 현재칸으로 오는 경우 = dpList[i-2]+stairList[i]
2) 현재-1 칸에서 현재칸으로 오는 경우 (무조건 현재-3에서 현재-1로 점프해야하기 때문에) = dpList[i-3]+stairList[i-1]+stairList[i]
"""