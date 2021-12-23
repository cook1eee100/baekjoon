import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m=map(int, input().split())
    rat = list(map(int, input().split()))

    answer=0
    while rat:
        check=0
        for i in range(1, len(rat)):
            if rat[i]>rat[0]:
                check=1
                break
        
        if check==0:
            rat.pop(0)
            answer+=1
            if m==0:
                print(answer)
                break
            else:
                m-=1

        else:
            rat.append(rat.pop(0))
            m= (m-1)%len(rat)


            
"""
m 의 값(target)을 rat과 똑같은 길이의 리스트(checkList)로 만들어서 m의 위치의 값만 1 나머진 0으로하고

rat 작업과 똑같이 pop 하고 append(pop) 함

그 와중에 체크는 checkList[0] 이 1일 때인지 아닌지 체크


# 다른 사람 풀이
test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    imp = list(map(int, input().split( )))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))  
            
"""