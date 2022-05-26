# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  """
  """
  counter = 0
  counter_max = 0
  prev_val = None
  
  curr = head
  while curr:
    if curr.val == prev_val:
      counter += 1
    else:
      counter = 1
      
    if counter > counter_max:
      counter_max = counter
      
    prev_val = curr.val
    curr = curr.next
    
  return counter_max
