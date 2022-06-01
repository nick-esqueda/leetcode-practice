class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def lowest_common_ancestor(root, val1, val2):
  """
  val1 or val2 could be the LCA
  get the path to val1 and the path to val2
  the first node that is common in both paths is the LCA
  """
  val1_path = get_path(root, val1)
  val2_path = get_path(root, val2)
  
  val1_set = set(val1_path)
  for val in val2_path:
    if val in val1_set:
      return val
  
def get_path(node, target):
  if not node:
    return None
  
  if node.val == target:
    return [node.val]
  
  left_path = get_path(node.left, target)
  if left_path:
    left_path.append(node.val)
    return left_path
  
  right_path = get_path(node.right, target)
  if right_path:
    right_path.append(node.val)
    return right_path
  
  return None

  
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

print(lowest_common_ancestor(a, 'd', 'h') )
