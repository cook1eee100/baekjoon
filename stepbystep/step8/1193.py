# # 시간초과
# n=int(input())

# x=y=1
# count=1
# check=0

# while n!=count:
#     count+=1
#     if x==y==1:
#         y+=1
#         continue

#     elif x==1:
#         r=y
#         for idx in range(r,1,-1):
#             x+=1
#             y-=1
#             if count==n:
#                 check=1
#                 break
#         if not check:
#             x+=1
#             count+=1

#     elif y==1:
#         r=x
#         for idx in range(r,1,-1):
#             x-=1
#             y+=1
#             if count==n:
#                 check=1
#                 break
#         if not check:
#             y+=1
#             count+=1

# print(f"{x}/{y}")


# 다른 사람 코드
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')