import sys
input = sys.stdin.readline

dwarfList=[]
for i in range(9):
    dwarfList.append(int(input()))

dwarfList.sort()
tempList=[]
remainder = sum(dwarfList)-100
for idx1 in range(len(dwarfList)-1):
    check=False
    for idx2 in range(idx1, len(dwarfList)):
        if dwarfList[idx1]+dwarfList[idx2]==remainder:
            tempList.append(dwarfList[idx1])
            tempList.append(dwarfList[idx2])
            check=True
            break
    if check==True:
        break

for i in dwarfList:
    if i not in tempList:
        print(i)

"""
9명 중 7명이 100이 된다는 건 
9명 총합에서 100을 빼면 나머지 2명의 키라는것
sum(dwarfList)-100 = 남은 2명의 드워프 키 합
"""