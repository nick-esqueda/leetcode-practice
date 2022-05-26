class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  new_node = Node(value)
  if index == 0:
    new_node.next = head
    return new_node
  
  i = 0
  curr = head
  while curr:
    if i + 1 == index:
      nxt = curr.next
      curr.next = new_node
      new_node.next = nxt
    curr = curr.next
    i += 1
    
  return head
