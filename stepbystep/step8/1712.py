# 시간초과
# a, b, c = map(int, input().split())

# if b>=c:
#     print(-1)
#     exit()

# idx=1
# while True:
#     if a+b*idx < c*idx:
#         break
#     idx+=1
# print(idx)


# 반복문을 돌릴 필요가 없음
import sys

a, b, c = map(int, sys.stdin.readline().split())

if b>=c:
    print(-1)
    exit()

print(a//(c-b)+1)

