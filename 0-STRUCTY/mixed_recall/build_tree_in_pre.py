class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if not in_order or not pre_order:
    return None
  
  root_val = pre_order.pop(0)
  root_in = in_order.index(root_val)
  
  left_in = in_order[:root_in]
  right_in = in_order[root_in + 1:]
  left_pre = pre_order[:len(left_in)]
  right_pre = pre_order[len(left_in):]
  
  root = Node(root_val)
  root.left = build_tree_in_pre(left_in, left_pre)
  root.right = build_tree_in_pre(right_in, right_pre)
  return root
  
