class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  """
  create dummy node with a tail pointer to start the loop
  for each value in values:
    create a new node with that value
    set tail.next to that new node
    move tail up to the new node
  """
  dummy = Node(0)
  tail = dummy
  for value in values:
    new_node = Node(value)
    tail.next = new_node
    tail = tail.next
    
  return dummy.next
  
