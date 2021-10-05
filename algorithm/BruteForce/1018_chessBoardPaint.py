import sys
input = sys.stdin.readline

n, m = map(int, input().split())

chessBoard=[]
for i in range(n):
    chessBoard.append(input())

answerList=[]
for idx1 in range(n-7):
    for idx2 in range(m-7):
        firstW=0
        firstB=0
        for i in range(idx1, idx1+8):
            for j in range(idx2, idx2+8):
                if (i+j)%2==0:
                    if chessBoard[i][j] !='W':
                        firstW+=1
                    if chessBoard[i][j] !='B':
                        firstB+=1
                else:
                    if chessBoard[i][j] !='B':
                        firstW+=1
                    if chessBoard[i][j] !='W':
                        firstB+=1

        answerList.append(firstW)
        answerList.append(firstB)

print(min(answerList))



"""
2차원 배열에서 (i+j)%2를 활용해 대각선 사용

"""