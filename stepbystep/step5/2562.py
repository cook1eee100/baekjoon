# maxValue=0
# index=0
# for idx in range(9):
#     a = int(input())
#     if maxValue <a:
#         maxValue = a
#         index=idx+1

# print(maxValue)
# print(index)


a=[]
for _ in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a))+1)