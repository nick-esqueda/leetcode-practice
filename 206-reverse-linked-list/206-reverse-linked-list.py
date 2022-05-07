# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        make sure that we have a head to begin with
        set prev pointer to null
        set curr pointer to head
        set next pointer to head.next
        while curr
          move next up one
          set curr's next to prev
          set prev as curr
        
        return prev
          
        
        
        EDGE CASES:
        there's no head
        there's only one node
        
        ?:
        what conditional to for while loop?
        
        """
        
        prev = None
        curr = head
        next = head
        while curr:
          next = curr.next 
          curr.next = prev
          prev = curr
          curr = next
          
        return prev