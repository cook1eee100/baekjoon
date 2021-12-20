import sys
input = sys.stdin.readline

n=int(input())
nList=list(map(int, input().split()))
nList.sort()
m=int(input())
mList=list(map(int, input().split()))

# 정렬 된 배열에서 찾고자 하는 값 이상이 처음 나타나는 위치         찾고자 하는 값의 시작위치
# nList[k-1] < num 이고 nList[k]>=num 인 k를 찾는다
def lowerBound(nList, num):
    start=0
    end=n

    while start<end:   #left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid=(start+end)//2

        if nList[mid]<num:
            start=mid+1
        else:
            end=mid
    return end


# 정렬 된 배열에서 찾고자 하는 값보다 큰 값이 처음 나타나는 위치    찾고자 하는 값의 마지막 index에 +1 한 위치
# nList[k] > num 을 만족하는 최소 k를 찾는다
def upperBound(nList, num):
    start=0
    end=n

    while start<end:
        mid=(start+end)//2

        if nList[mid]<=num:
            start=mid+1
        else:
            end=mid

    return end

for num in mList:
    print(upperBound(nList,num)-lowerBound(nList,num))




"""

lowerbound에서 찾을 값의 시작위치 알아내고 upperbound에서 찾을값보다 큰값의 시작위치를 알아내서
upperbound에서 lowerbound를 빼면 됨


딕셔너리 사용해서 각 값의 개수 카운팅해서 구해도 됨 (Counter 클래스 사용)
"""