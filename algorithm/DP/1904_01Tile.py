import sys
input = sys.stdin.readline

n = int(input())

dpList=[0 for _ in range(1000001)]
dpList[1]=1
dpList[2]=2

for i in range(3, n+1):
    dpList[i] = (dpList[i-1]+dpList[i-2])%15746
    
print(dpList[n])







"""
1   1   1
2   2   00, 11
3   3   001, 100, 111
4   5   0000, 1111, 0011, 1100, 1001



**** 나머지를 계산중에 넣자! (메모리 초과가 일어남)
    0 for _ in range(n+1)로 할 경우 n이 0 일때 dpList[1] 참조에서 문제가 생김

"""