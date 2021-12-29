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

nodeList=[]
for i in range(n):
    temp = input().strip().split()
    # print(temp)
    nodeList.append(Node(temp[0]))

for i in nodeList:
    print(i)





"""     # 트리 구현 없이 단순히 dfs 재귀로 푼 코드

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