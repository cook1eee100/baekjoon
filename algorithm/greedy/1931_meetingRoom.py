n = int(input())
answer=0

meetingList=[]
for _ in range(n):
    s, e = map(int, input().split())
    meetingList.append([e, s])

meetingList.sort()

endTime = 0
for e, s in meetingList:
    if endTime<=s:
        endTime=e
        answer+=1

print(answer)