s = input()

alphaList=[0]*26

for idx in range(len(s)):
    if ord('a')<=ord(s[idx])<=ord('z'):
        alphaList[ord(s[idx])-ord('a')]+=1
    else:
        alphaList[ord(s[idx])-ord('A')]+=1

reverseList=sorted(alphaList, reverse=True)
if reverseList[0]==reverseList[1]:
    print('?')
else:
    print(chr(alphaList.index(max(alphaList))+ord('A')))

