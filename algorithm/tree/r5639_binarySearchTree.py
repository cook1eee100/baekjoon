import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

def solution(start, end, nums):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        if nums[start] < nums[i]:
            div = i
            break

    solution(start + 1, div - 1, nums)
    solution(div, end, nums)
    print(nums[start])

nums=[]
while True:
    try:
        nums.append(int(input()))

    except:
        break

solution(0, len(nums)-1, nums)


"""
    트리 특성 이용 (전위, 후위 특징)

    현재 노드 값 기준으로

    현재 노드 데이터는 root,
    현재 노드 데이터보다 큰 값이 이후의 데이터는 현재 트리의 오른쪽 서브 트리
    그 전까지 왼쪽 서브트리

"""