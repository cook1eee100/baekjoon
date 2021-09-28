import sys
input = sys.stdin.readline

n = int(input())
dpList=[0]*(n+1)

for i in range(2, n+1):
    dpList[i] = dpList[i-1]+1

    if i%3==0:
        dpList[i] = min(dpList[i//3]+1, dpList[i])
    if i%2==0:
        dpList[i] = min(dpList[i//2]+1, dpList[i])
    
print(dpList[n])





"""
반복문 내에서 작업
dplist에 기본적으로 전 수에다가 +1한 처리 횟수 1을 추가해서 넣어놓고
i%3==0 일 때 x//3의 수에다가 *3 한 처리 횟수 1을 추가해서 값 비교 
i%2==0 일 때 x//2의 수에다가 *2 한 처리 횟수 1을 추가해서 값 비교
"""