class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  """
  """
  dummy = Node(0)
  dummy_tail = dummy
  curr_1 = head_1
  curr_2 = head_2
  while curr_1 and curr_2:
    if curr_1.val < curr_2.val:
      dummy_tail.next = curr_1
      curr_1 = curr_1.next
    else:
      dummy_tail.next = curr_2
      curr_2 = curr_2.next
    
    dummy_tail = dummy_tail.next
    
  if curr_1:
    dummy_tail.next = curr_1
  if curr_2:
    dummy_tail.next = curr_2
    
  return dummy.next


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

merge_lists(a, q)
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
