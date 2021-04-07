s= input()

alphaList=[-1]*26

a=ord('a')
for idx in range(len(alphaList)):
    alphaList[idx]=s.find(chr(a))
    a+=1
   
for alpha in alphaList:
    print(alpha, end=" ")