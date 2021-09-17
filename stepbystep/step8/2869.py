# # 시간초과
# a, b, v = map(int, input().split())

# day=0
# total=0
# while True:
#     day+=1
#     total+=a
#     if total >= v:
#         break
#     total-=b

# print(day)

# 다른 사람 코드
a, b, v = map(int, input().split())

ls = 0
if (v-b)%(a-b)!=0:
    ls=((v-b)//(a-b))+1
else:
    ls=((v-b)//(a-b))
print(ls)