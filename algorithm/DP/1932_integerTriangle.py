import sys
input = sys.stdin.readline

n=int(input())
integerList=[]
for i in range(n):
    integerList.append(list(map(int, input().split())))

idx=2
for i in range(1, n):
    for j in range(idx):
        if j==0:
            integerList[i][j]+=integerList[i-1][j]
        elif i==j:
            integerList[i][j]+=integerList[i-1][j-1]
        else:
            integerList[i][j]+=max(integerList[i-1][j-1], integerList[i-1][j])
    idx+=1
print(max(integerList[n-1]))



"""
				0 0
			1 0		1 1
		2 0		2 1		2 2
	3 0		3 1		3 2		3 3
4 0		4 1		4 2		4 3		4 4
"""