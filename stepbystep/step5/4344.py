c = int(input())


for _ in range(c):
    gradeList=list(map(int, input().split()))
    
    total=0
    average = 0
    for idx in range(1, gradeList[0]+1):
        total+=gradeList[idx]
    average = total/gradeList[0]

    student=0
    for grade in gradeList[1:]:
        if grade > average:
            student+=1
    
    print("%.3f%%" % (student/gradeList[0]*100))


