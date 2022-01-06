import sys
input = sys.stdin.readline



if __name__=="__main__":
    n, m, b=map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]

    blockDict={}

    for i in range(n):
        for j in range(m):
            if graph[i][j] not in blockDict.keys():
                blockDict[graph[i][j]]=1
            else:
                blockDict[graph[i][j]]+=1

    minValue=min(blockDict.keys())
    maxValue=max(blockDict.keys())

    answer=[1e9,0]
    for h in range(minValue, maxValue+1):
        t=0
        bag=b
        for i in blockDict.keys():
            if i>h:
                t+= (i-h)*2*blockDict[i]
                bag+=(i-h)*blockDict[i]
            elif i<h:
                t+= (h-i)*blockDict[i]
                bag-=(h-i)*blockDict[i]

        if bag<0:
            continue

        if answer[0]>=t:
            answer=[t, h]
    print(answer[0], answer[1])


























"""

    # 시간초과

if __name__=="__main__":
    n, m, b=map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]

    minValue=1e9
    maxValue=-1e9
    for i in range(n):
        minValue=min(minValue, min(graph[i]))
        maxValue=max(maxValue, max(graph[i]))
    
    answer=[1e9, 0]
    for k in range(maxValue, minValue-1, -1):
        t=0
        bag=b
        for i in range(n):
            for j in range(m):
                if k>graph[i][j]:
                    t+=(k-graph[i][j])
                    bag-=(k-graph[i][j])
                elif k<graph[i][j]:
                    t+=(graph[i][j]-k)*2
                    bag+=(graph[i][j]-k)
        
                if answer[0]<t:
                    break

            else:
                continue
            break
        
        if bag<0:
            continue

        if t<answer[0]:
            answer=[t, k]
        
        
    
    print(answer)

"""

