import sys
input = sys.stdin.readline

n= int(input())
wineList=[0]
for i in range(n):
    wineList.append(int(input()))

dpList=[0]
for i in range(1, n+1):
    if i==1:
        dpList.append(wineList[i])
    elif i==2:
        dpList.append(wineList[i-1]+wineList[i])
    else:
        dpList.append(max(dpList[i-1], dpList[i-2]+wineList[i], dpList[i-3]+wineList[i-1]+wineList[i]))
print(max(dpList))



"""

1) 해당 순서의 포도주를 마시는 경우 (백준 2579 계단 오르기형태)
    1-1) 현재-2 칸에서 현재-1 칸을 뛰고 현재 칸도 먹는 경우 = dpList[i-2]+wineList[i]
    1-2) 현재-1 칸을 먹고 현재 칸도 먹는 경우 (현재-3 칸에서 현재-1 칸으로 뜀) = dpList[i-3]+wineList[i-1]+wineList[i]
2) 해당 순서의 포도주를 마시지 않는 경우 (백준 2579 계단 오르기와 다른점은 계단에서는 해당 칸을 무조건 밟아야 했기때문에 이 경우를 제외하는 듯?)
    현재 포도주를 먹지 않는다는건 바로 전 포도주를 먹은 경우(바로 전 포도주의 최대값으로 계산) = dpList[i-1]
"""