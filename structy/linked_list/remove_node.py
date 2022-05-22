# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  """
  what about deleting the head?
  prev pointer, curr pointer
  loop through the LL 
    move prev to curr and curr to curr.next on each iteration
    if curr.val == target...
      save curr.next in a temp var
      (do you need to sever the connection between curr and temp?)
      set prev.next to the temp var
      return the LL head
  """
  if head.val == target_val:
    return head.next
  
  prev = None
  curr = head
  while curr:
    if curr.val == target_val:
      nxt = curr.next
      prev.next = nxt
      return head
      
    prev = curr
    curr = curr.next
