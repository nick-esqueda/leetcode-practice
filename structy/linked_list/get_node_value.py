# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  i = 0
  curr = head
  while curr:
    if i == index:
      return curr.val
    curr = curr.next
    i += 1


def get_node_value(head, index):
  if head is None:
    return
  if index == 0:
    return head.val
  
  return get_node_value(head.next, index - 1)
