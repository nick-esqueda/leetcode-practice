# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):
  vals = []
  cur = head
  while cur:
    vals.append(cur.val)
    cur = cur.next
  
  return vals == vals[::-1]
  
