# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        assign head.next to the node that normally comes next, UNLESS it's the node we want to delete
        if you realize that the current node is the one you need to delete, return cur.next 
            this is so that the recursive caller get's back the NEXT next node, instead of the OG next node
        else if the current node isn't the one you want to delete, return the curr node as it is
        you can tell which node you want to delete/where you are by keeping track of a position variable
            that you can increment after the recursive call
        if this current position == n, then this is the node you want to delete, so return curr.next
        """
        def delete_n(head):
            if head is None:
                return (None, 0)
            
            head.next, next_pos = delete_n(head.next)
            curr_pos = 1 + next_pos
            
            if curr_pos == n:
                return (head.next, curr_pos)
            else:
                return (head, curr_pos)
            
        return delete_n(head)[0]
        
        
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