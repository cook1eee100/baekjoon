n = int(input())

oxList=[]
for idx in range(n):
    oxList.append(input())

for ox in oxList:
    result=0
    i=0
    for idx in range(len(ox)):
        if ox[idx] == 'O':
            i+=1
            result+=i
        else:
            i=0
    print(result)