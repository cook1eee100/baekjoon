n = int(input())

dpList=[0, 1, 3]

for i in range(3, n+1):
    dpList.append(dpList[i-1]+dpList[i-2]*2)

print(dpList[n]%10007)




"""
0   0
1   1
2   3
3   5
4   11


"""