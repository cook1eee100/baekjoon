import sys
input = sys.stdin.readline

n = int(input())

dpList=[0,1,2]
for i in range(3, n+1):
    dpList.append(dpList[i-1]+dpList[i-2])
answer=dpList[n]%10007
print(answer)



