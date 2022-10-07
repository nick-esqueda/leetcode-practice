class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  """
  the middle of the in_order array is the root
  if you take the left from the middle of the in_order arr you get the left subtree, 
  the last post order node is the root
  the two traversals have all the subtree nodes within the same range
    first 3 nodes of in order are same as first 3 of post
  
  if inorder or postorder have no len, return None
  pop the last post_order node to be root
  find the idx of that root in the in order trav
  save the len up to the root in the in order trav (left subtree)
  take the same len from the post order (0 - len)
  save the len after the root to end of in order trav (right subtree)
  take the remaining of post order (since you popped the last/root)
  recurse with the left and right in orders and post orders
  
  return the root of the new tree
  """
  if not in_order or not post_order:
    return None
  
  root_val = post_order.pop()
  root_io_idx = in_order.index(root_val)
  
  left_io = in_order[:root_io_idx]
  right_io = in_order[root_io_idx + 1:]
  left_po = post_order[:root_io_idx]
  right_po = post_order[root_io_idx:]
  
  root = Node(root_val)
  root.left = build_tree_in_post(left_io, left_po)
  root.right = build_tree_in_post(right_io, right_po)
  
  return root
  
