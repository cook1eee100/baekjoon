t = int(input())

for _ in range(t):
    n = int(input())
    
    recruitList=[]
    for _ in range(n):
        recruitList.append(list(map(int, input().split())))

    recruitList.sort()
    print(recruitList)