# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def is_binary_search_tree(root):
  vals = []
  
  def dfs(root):
    if not root:
      return
    
    dfs(root.left)
    vals.append(root.val)
    dfs(root.right)
    
  dfs(root)
  return is_ordered(vals)
  
def is_ordered(vals):
  i = 0
  j = 1
  while j < len(vals):
    if vals[i] > vals[j]:
      return False
    i += 1
    j += 1
    
  return True
