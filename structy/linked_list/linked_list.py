# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  vals = []
  curr = head
  while curr:
    vals.append(curr.val)
    curr = curr.next
  return vals


def linked_list_values(head):
  vals = []
  get_values(head, vals)
  return vals

def get_values(head, values):
  if not head:
    return
  values.append(head.val)
  get_values(head.next, values)
