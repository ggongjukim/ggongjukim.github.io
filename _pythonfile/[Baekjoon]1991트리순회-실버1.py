#이진트리를 입력받아 전위순회 중위순회 후위순회 결과를 출력해라

N = int(input())
tree = {}
class Node:
  def __init__(self,item,left=None, right=None):
    self.val = item
    self.left = left
    self.right = right

for _ in range(N):
  root, l, r = list(map(str, input().split()))
  if l == '.':
    l = None
  if r == '.':
    r = None
  tree[root] = Node(root, l,r)

def pre(cur): #부 왼 오오
 if cur is None:
   return

 print(cur.val, end='')
 if cur.left:
   pre(tree[cur.left])
 if cur.right:
   pre(tree[cur.right])

def In(cur):#왼 부 오
  if cur is None:
    return

  if cur.left:
    In(tree[cur.left])
  print(cur.val,end='')
  if cur.right:
    In(tree[cur.right])

def post(cur):# 왼 오 부
  if cur is None:
    return
  if cur.left:
    post(tree[cur.left])
  if cur.right:
    post(tree[cur.right])
  print(cur.val,end='')

pre(tree['A'])
print()
In(tree['A'])
print()
post(tree['A'])