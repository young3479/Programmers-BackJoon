#예시 입력
"""""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""""

#트리 입력 받기
N = int(input())
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
#print(tree)

def preorder(root):
    if root == '.':
        return
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == '.':
        return
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
    if root == '.':
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

#항상 A가 루트 노드가 됨
preorder('A')
print()
inorder('A')
print()
postorder('A')