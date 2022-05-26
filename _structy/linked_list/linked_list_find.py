# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  if head is None:
    return False
    
  if head.val == target:
    return True
  else:
    return linked_list_find(head.next, target)

  
def linked_list_find(head, target):
  curr = head
  while curr:
    if curr.val == target:
      return True
    curr = curr.next
    
  return False
