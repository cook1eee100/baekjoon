numberList=[]
for idx in range(10):
    numberList.append(int(input()))
    numberList[idx] %= 42

print(len(set(numberList)))

