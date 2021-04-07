n = int(input())

count=0
for _ in range(n):
    word = input()
    alphaList=[]
    for idx, alpha in enumerate(list(word)):
        if idx==0:
            alphaList.append(alpha)
        else:
            if word[idx-1] == word[idx]:
                continue
            
            if alpha in alphaList:
                count-=1
                break
            alphaList.append(alpha)
    count+=1
print(count)



# 다른사람 코드
a = int(input())
al = 0
for i in range(a):
    b = input()
    A = [0]
    answer = 1
    bk = 0
    for j in range(len(b)):
        if (b[j] in A) == True:
            if b[j] != b[j-1]:
                answer = 0
                break
        else:
            A.append(b[j])
    if answer == 1:
        al+=1
print (al)