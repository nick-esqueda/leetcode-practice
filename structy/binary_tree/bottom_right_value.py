class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

def bottom_right_value(root):
  """
  declare var to hold the current level's right most val
  iterate breadth first so that you can keep track of levels
    for however long the queue is (loop), popleft and add children
    on the last iteration of the inner loop, reassign rightmost var
  after iterating, return the rightmost var as the last level will have been most recent
  """
  rightmost = root.val
  q = deque([root])
  while q:
    len_q = len(q)
    for i in range(len_q):
      curr = q.popleft()
      
      if i == len_q - 1:
        rightmost = curr.val
        
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
        
  return rightmost
  
  
a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

bottom_right_value(a) # -> 1
