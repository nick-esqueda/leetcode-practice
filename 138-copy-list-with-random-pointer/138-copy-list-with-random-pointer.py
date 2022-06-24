"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]', copies={}) -> 'Optional[Node]':
        """
        go through and copy each node's values verbatim
        each new node's next and random pointers should point to the nodes in the new list, not the old one
        
        if the cur node is in the map, just return cur's copy
        create a new node using the class and cur node's val
        put the new node mapped to the old node in a HM
        assign the new node's .next to the return of recursive call
        assign the new node's .random to theh return of another recursive call
        return the copy node
        """
        if not head:
            return None
        if head in copies:
            return copies[head]

        copy = Node(head.val)
        copies[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.copyRandomList(head.random)
        return copy
