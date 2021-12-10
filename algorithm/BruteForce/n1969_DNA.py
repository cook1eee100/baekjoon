import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna=['A', 'T', 'G', 'C']
DNAList=[]
for i in range(n):
    DNAList.append(list(input().strip()))

DNACount=[[0 for _ in range(4)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        for idx in range(dna):
            if DNAList[j][i] == dna[idx]:
                pass
