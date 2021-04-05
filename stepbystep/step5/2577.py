a = int(input())
b = int(input())
c = int(input())

numberList=[0]*10

for idx in list(str(a*b*c)):
    numberList[int(idx)]+=1

for idx in numberList:
    print(idx)

# result=list(str(a*b*c))
# for i in range(10):
#     print(result.count(str(i)))