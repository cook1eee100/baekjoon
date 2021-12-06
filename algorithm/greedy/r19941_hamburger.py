# n, k = map(int, input().split())

# table = list(input().strip())

# answer=0
# for i in range(len(table)):
#     if table[i]=='P':
#         for j in range(i-k, i+k+1, 1):
#             if 0<=j<n and table[j]=='H':
#                 answer+=1
#                 table[j]='0'
#                 break
# print(answer)



import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tableList=list(input().strip())

answer=0
for i in range(n):
    if tableList[i]=='P':
        for j in range(i-k, i+k+1):
            if 0<= j <n:
                if tableList[j]=='H':
                    tableList[j]='0'
                    answer+=1
                    # print(i, j)
                    # print(tableList)
                    break
                    
print(answer)
                

"""
사람을 기준으로 범위 안에 햄버거가 있는지 없는지 체크하고 햄버거 값을 바꿈

중복으로 여러개 먹을 수 있으니 break 걸어서 처음 먹은것만 바꾸게 함
"""