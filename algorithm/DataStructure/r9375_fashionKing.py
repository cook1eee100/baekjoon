import sys
input = sys.stdin.readline



if __name__=="__main__":
    t= int(input())

    for _ in range(t):
        n = int(input())
        fashion={}
        for _ in range(n):
            a, b = input().strip().split()
            if b not in fashion.keys():
                fashion[b]=[a]
            elif b in fashion.keys():
                fashion[b].append(a)
        # print(fashion)

        
        answer=1
        for i in fashion.keys():
            answer*=(len(fashion[i])+1)
        print(answer-1)




"""

조합론

같은 종류의 의상은 하나씩만 착용할 수 있으며, 알몸이 아니어야 하므로 꼭 1종류 이상의 의상은 착용해야 한다.

예를 들어, 3종류의 의상이 있으면 1종류만 착용해도 되며, 2종류를 착용해도 되고, 3종류를 착용해도 되지만 0종류를 착용하는건 안된다.

 

그렇다면 다음과 같은 식을 세울 수 있다.

(a종류수 + 1) * (b종류수 + 1) * (c종류수 + 1)... - 1

 

여기서 종류수에 +1을 해준 이유는 그 종류의 의상을 착용해도 되고 안해도 되기 때문이고

마지막에 -1을 해준 이유는 모든 의상을 착용하지 않은 경우를 제외시켜줘야 하기 때문이다.

"""