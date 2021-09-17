money = 1000 - int(input())

changeList=[500, 100, 50, 10, 5, 1]

answer=0
for i in changeList:
    answer+= money//i
    money=money%i

print(answer)