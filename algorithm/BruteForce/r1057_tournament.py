# import sys
# input = sys.stdin.readline

# n, kim, im = map(int, input().split())

# proList=[i for i in range(1, n+1)]
# answer=1
# while n!=0:
#     tempList=[]
#     # print(proList)
#     for i in range(0, (n//2)*2, 2):           // 여기서 문제인듯 홀수인 경우에??? 아닌 데?
#         # print(proList[i], proList[i+1])
#         if proList[i] in [kim,im] and proList[i+1] in [kim, im]:
#             print(answer)
#             n=0
#             break
    
#         if proList[i] in [kim, im]:
#             tempList.append(proList[i])
#         elif proList[i+1] in [kim, im]:
#             tempList.append(proList[i+1])
#         else:
#             tempList.append(proList[i])

#     else:
#         if len(proList)%2!=0:
#             tempList.append(proList[-1])
#         proList=tempList
#         n//=2
#         answer+=1
#         continue

#     break



import sys
input = sys.stdin.readline

n, kim, im = map(int, input().split())

count=0
while kim!=im:
    kim-=kim//2
    im-=im//2
    count+=1
print(count)


"""

토너먼트 규칙??
   -
 -   -
 2   4
- - - -
1 2 3 4

2, 4

2 1 1
4 2 1
"""