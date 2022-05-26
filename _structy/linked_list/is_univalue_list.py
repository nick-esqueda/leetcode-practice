class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  curr = head
  first_val = head.val
  while curr:
    if curr.val != first_val:
      return False
    curr = curr.next
  return True


def is_univalue_list(head, prev_val=None):
  if head is None:
    return True
  
  if prev_val is None or head.val == prev_val:
    return is_univalue_list(head.next, head.val)
  else:
    return False
  
  
u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

is_univalue_list(u) # True
