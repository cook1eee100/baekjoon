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

