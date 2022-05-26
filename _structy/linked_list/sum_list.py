# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  total = 0
  curr = head
  while curr:
    total += curr.val
    curr = curr.next
  return total


def sum_list(head):
  if not head:
    return 0
  return head.val + sum_list(head.next)
