# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):
  """
  [len // 2]
  """
  vals = []
  cur = head
  while cur:
    vals.append(cur.val)
    cur = cur.next
    
  return vals[len(vals) // 2]
