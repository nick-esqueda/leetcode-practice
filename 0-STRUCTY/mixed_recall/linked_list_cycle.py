class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_cycle(head, visited=set()):
  if not head:
    return False
  if head.val in visited:
    return True
  visited.add(head.val)
  return linked_list_cycle(head.next)

def linked_list_cycle(head):
  visited = set()
  
  cur = head
  while cur:
    if cur.val in visited:
      return True
    visited.add(cur.val)
    cur = cur.next
    
  return False

def linked_list_cycle(head):
  """
  use a fast and slow pointer (both set to head at first)
  on each iteration, move slow up one, but fast up two
  if fast ever == slow, you have a loop
  if fast gets to the end, no loops
  """
  first_iter = True
  slow = head
  fast = head
  while fast and fast.next:
    if slow == fast and not first_iter:
      return True
    slow = slow.next
    fast = fast.next.next
    first_iter = False
    
  return False
