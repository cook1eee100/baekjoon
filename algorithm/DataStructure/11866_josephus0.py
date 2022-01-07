import sys
input = sys.stdin.readline



if __name__=="__main__":
    n, k = map(int, input().split())
    graph=[i for i in range(1, n+1)]

    answer=[]
    i=0
    while graph:
        i+=k-1

        if i>=len(graph):
            i=i%len(graph)

        answer.append(graph.pop(i))

    print("<"+", ".join(list(map(str, answer)))+">")



"""
    1 2 3 4 5 6 7

    k v l   g
    2 3 6   1 2 4 5 6 7
    4 6 5   1 2 4 5 7
    1 2 4   1 4 5 7
    3 7 3   1 4 5
    2

"""