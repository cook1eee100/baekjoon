import sys
input = sys.stdin.readline

n=int(input())
consultingList=[]
for _ in range(n):
    consultingList.append(list(map(int,input().split())))

dpList=[0 for i in range(n+1)]
for i in range(n-1, -1, -1):
    if consultingList[i][0] + i>n:
        dpList[i]=dpList[i+1]
    else:
        dpList[i]=max(dpList[i+1], consultingList[i][1]+dpList[i+consultingList[i][0]])
print(dpList[0])




"""
문제랑 dpList 결과 값 보면서 이해
뒤에서부터 dp로 접근
경우의 수는 상담기간이 길어서 마지막 날이 기간이 지나서 못할 때와 지나지 않아서 할 수 있을 때
1) 못할 때 = 다음날의 dp값을 현재의 dp 값으로           (정확하게 이해가 안됨)
2) 할수 있을 때 = 다음날의 dp값과 현재상담 비용+현재 상담이 끝난 날 dp값 비교해서 더 큰수를 현재 dp값으로

이해가 안됨

"""