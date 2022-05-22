# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  curr = head
  prev = None
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
  return prev
  

def reverse_list(head, prev=None):
  if head is None:
    return prev
  
  nxt = head.next
  head.next = prev
  return reverse_list(nxt, head)
  