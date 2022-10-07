class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  """
  set curr1 and curr2 to heads of both lists
  set tail pointer to curr1 head
  count = 0
  while curr1 and curr2
    if count is even:
      c1 == c1.next
      tail.next = c2
    if count is odd:
      c2 == c2.next
      tail.next = c1
    both:
      tail = tail.next
      count += 1
  """    
  count = 0
  curr_1 = head_1
  curr_2 = head_2
  tail = curr_1
  while curr_1 and curr_2:
    if count % 2 == 0:
      curr_1 = curr_1.next
      tail.next = curr_2
    if count % 2 == 1:
      curr_2 = curr_2.next
      tail.next = curr_1
      
    tail = tail.next
    count += 1
    
  return head_1
  
    
a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z
