import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[list(map(int, list(input().strip()))) for _ in range(n) ]

answer=0
for i in range(n):
    for j in range(m):

        for idx in range(j, m):
            if i+(idx-j)>=n:
                break
            s1=graph[i][j]
            s2=graph[i][idx]
            s3=graph[i+(idx-j)][j]
            s4=graph[i+(idx-j)][idx]


            if s1==s2==s3==s4:
                temp=(idx-j+1)*(idx-j+1)
                # print(s1, temp)
                # print(f"({i}, {j}), ({i}, {idx}), ({i+(idx-j)}, {j}), ({i+(idx-j)}, {idx})")


                if answer<temp:
                    answer=temp

print(answer)


"""
MAX = min(n, m)  이걸로 행 열 중 어느게  더 작은지 체크 가능

for i in range(n):
    for j in range(m):
        for k in range(MAX):
            if i+k <n and j+k < m:  범위 체크
                i,j     i, j+k      i+k, j      i+k, j+k


"""
