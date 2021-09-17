s = int(input())

# total=0
# i=1
# while total<=s:
#     total+=i
#     print("total, i : ", total, i)
#     i+=1
# print(i-1)

total=0
i=0
while total<=s:
    i+=1
    total+=i
    print("total, i : ", total, i)
    
print(i-1)