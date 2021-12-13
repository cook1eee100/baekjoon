import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna=['A', 'C', 'G', 'T']
DNAList=[]
for i in range(n):
    DNAList.append(list(input().strip()))

DNACount=[[0 for _ in range(4)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        for idx in range(len(dna)):
            if DNAList[j][i] == dna[idx]:
                DNACount[i][idx]+=1

answerDNA=""
answer=0
for idx in range(len(DNACount)):
    answerDNA+=dna[DNACount[idx].index(max(DNACount[idx]))]
    answer+=(n-max(DNACount[idx]))

print(answerDNA)
print(answer)



"""
문자 관련 문제는 26개 인덱스의 리스트 만들어서 각 문자 카운팅 해도 됨
"""