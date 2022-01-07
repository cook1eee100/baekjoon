import sys
input = sys.stdin.readline


if __name__=="__main__":
    n, m = map(int ,input().split())
    noSeeList=set(input().strip() for _ in range(n))
    noListenList=set(input().strip() for _ in range(m))
    
    answer=sorted(noSeeList&noListenList)

    print(len(answer))
    for i in answer:
        print(i)




"""
    리스트로 하나하나씩 존재하는지 체크하면 시간오류남

    set으로 & 연산통해서 교집합 찾아내기

"""