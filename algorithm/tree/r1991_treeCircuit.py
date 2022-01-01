# 트리로 안풀고 걍 재귀로 품
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root=None

    def makeTree(self, node, leftNode, rightNode):
        if self.root==None:
            self.root=node
        self.left=leftNode
        self.right=rightNode

    def preorderTraversal(self):pass
        

n = int(input())

nodeDict={}
for i in range(n):
    node, left, right=input().strip().split()
    nodeDict[node]=[left, right]







"""     # 트리 구현 없이 단순히 dfs 재귀로 푼 코드
        # 리스트로 하나하나 검색하지 말고 데이터를 넣을때 딕셔너리로 넣어서 값 체크 없이 바로 value로 다음 노드 넘어가기


import sys
input = sys.stdin.readline

def preorder(c, graph):
    print(c[0], end="")

    if not c[1]=='.':
        for i in range(len(graph)):
            if c[1] == graph[i][0]:
                preorder(graph[i], graph)

    if not c[2]=='.':
        for i in range(len(graph)):
            if c[2] == graph[i][0]:
                preorder(graph[i], graph)


def inorder(c, graph):

    if not c[1]=='.':
        for i in range(len(graph)):
            if c[1]==graph[i][0]:
                inorder(graph[i], graph)

    print(c[0], end="")

    if not c[2]=='.':
        for i in range(len(graph)):
            if c[2]==graph[i][0]:
                inorder(graph[i], graph)

def postorder(c, graph):

    if not c[1]=='.':
        for i in range(len(graph)):
            if c[1]==graph[i][0]:
                postorder(graph[i], graph)

    if not c[2]=='.':
        for i in range(len(graph)):
            if c[2]==graph[i][0]:
                postorder(graph[i], graph)
    
    print(c[0], end="")



n = int(input())
graph = [ input().strip().split() for _ in range(n)]

preorder(graph[0], graph)
print()
inorder(graph[0], graph)
print()
postorder(graph[0], graph)


"""