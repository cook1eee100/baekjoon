
import sys
input = sys.stdin.readline


n = int(input())
sequenceList=list(map(int, input().split()))

dpList=[x for x in sequenceList]

for i in range(n):
    for j in range(i):
        if sequenceList[i]>sequenceList[j]:
            dpList[i] = max(dpList[i], dpList[j]+sequenceList[i])
print(max(dpList))



"""
dp 문제

앞 dp 값들에 현재값을 더한거랑 현재 값 중에 큰거를 계속 갱신해가며 찾기

"""

