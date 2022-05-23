class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root, curr_min=float('inf')):
  if not root:
    return curr_min
  if root.val < curr_min:
    curr_min = root.val
  return min(tree_min_value(root.left, curr_min), tree_min_value(root.right, curr_min))


a = Node(3)
b = Node(11)
c = Node(4)
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
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value(a)) # -> -2
