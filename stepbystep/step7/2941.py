s=input()

croatiaList=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatiaList:
    s=s.replace(alpha,"a")
print(s)




# # 다른 방식으로
# count=0
# check=0

# for idx in range(len(s)-1):
#     if check != 0:
#         check-=1
#         continue

#     if s[idx]+s[idx+1] in croatiaList:
#         count+=1
#         check+=1
#         continue
  
#     elif s[idx]+s[idx+1]+s[idx+2] in croatiaList:
#         count+=1
#         check+=2
  
#     count+=1

# print(count)