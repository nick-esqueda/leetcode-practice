# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         """
#         assign head.next to the node that normally comes next, UNLESS it's the node we want to delete
#         if you realize that the current node is the one you need to delete, return cur.next 
#             this is so that the recursive caller get's back the NEXT next node, instead of the OG next node
#         else if the current node isn't the one you want to delete, return the curr node as it is
#         you can tell which node you want to delete/where you are by keeping track of a position variable
#             that you can increment after the recursive call
#         if this current position == n, then this is the node you want to delete, so return curr.next
#         """
#         def delete_n(head):
#             if head is None:
#                 return (None, 0)
            
#             head.next, next_pos = delete_n(head.next)
#             curr_pos = 1 + next_pos
            
#             if curr_pos == n:
#                 return (head.next, curr_pos)
#             else:
#                 return (head, curr_pos)
            
#         return delete_n(head)[0]
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        two pointers that are n distance apart
        whenever the right pointer is at None, you know that the left pointer is at the node you want to delete
        in order to get the node BEFORE the one you want to delete (since we need access to it),
        use a dummy node to act as the start
            the dummy node will prevent you from getting some .next.next errors, because you want the 
            left and right pointers to essentially be n + 1 nodes apart, but you might not be able to do
            .next.next since .next might be None. but if you have a dummy node, you can instead move the 
            left pointer back by one
        iterate both pointers through the list
        when right hits none, perform the delete
        """
        dummy = ListNode(0)
        dummy.next = head
        
        left, right = dummy, head
        while n != 0:
            right = right.next
            n -= 1
            
        while right is not None:
            left = left.next
            right = right.next
            
        new_nxt = left.next.next
        left.next = new_nxt
        return dummy.next
        
        
#     ITERATIVE O(2n)
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         """
#         get the len of LL by iterating once through and counting nodes
#         take len(LL) - n and that will be the 0-indexed INDEX that you need to remove
#         iterate until one before that index and then perform a deletion
#         """
        
#         def get_len(head, count=0):
#             if not head:
#                 return count
#             return 1 + get_len(head.next)
        
#         len_LL = get_len(head)
#         removal_idx = len_LL - n
        
#         cur = head
#         while cur:
#             if removal_idx == 0:
#                 head = head.next
#                 return head
#             if removal_idx == 1:
#                 old_nxt = cur.next
#                 new_nxt = old_nxt.next
#                 cur.next = new_nxt
#                 return head
#             removal_idx -= 1
#             cur = cur.next
        
#         return head