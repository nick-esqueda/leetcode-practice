class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  """
  curr1 = head1, curr2 = head2
  create dummy node for the new list with a tail pointer
  declare remainder var = 0
  while curr1 OR curr2 or remainder:
    num1 = 0 if curr1 is none, otherwise curr1.val
    num2 = 0 if curr2 is none, otherwise curr2.val
    sum = num1 + num2 + remainder
    remainder = 0 if sum < 10 else 1
    
    new_node = node(sum - 10) if remainder else node(sum)
    tail.next = new_node
    move tail up
    if curr1, move curr up
    if curr2, move curr up
  return dummy.next
  """
  dummy = Node(0)
  tail = dummy
  remainder = 0
  curr_1 = head_1
  curr_2 = head_2
  while curr_1 or curr_2 or remainder:
    num1 = 0 if curr_1 is None else curr_1.val
    num2 = 0 if curr_2 is None else curr_2.val
    sum = num1 + num2 + remainder
    remainder = 0 if sum < 10 else 1
    
    new_node = Node(sum - 10) if remainder else Node(sum)
    tail.next = new_node
    tail = tail.next
    
    if curr_1:
      curr_1 = curr_1.next
    if curr_2:
      curr_2 = curr_2.next
      
  return dummy.next
    
    
    
    
