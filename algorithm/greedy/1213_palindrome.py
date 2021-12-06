alphaList = list(input())

answer=""
tempList=[]
odd=""
for c in set(alphaList):
    tempList.append([c, alphaList.count(c)])
    if alphaList.count(c)%2!=0:
        odd+=c

tempList.sort()

if len(odd)>1:
    print("I'm Sorry Hansoo")

else:
    for c, cnt in tempList:
        answer+=c*(cnt//2)
    answer+=odd
    for c, cnt in reversed(tempList):
        answer+=c*(cnt//2)

print(answer)




"""
26개 인덱스의 리스트 만들고 해당 알파벳 리스트 카운트해서 개수 세고
홀 수 문자 체크하고

alpha+odd_alpha+alpha[::-1] 이런식으로도 가능

"""

