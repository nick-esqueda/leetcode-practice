# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        get the len of LL by iterating once through and counting nodes
        take len(LL) - n and that will be the 0-indexed INDEX that you need to remove
        iterate until one before that index and then perform a deletion
        """
        
        def get_len(head, count=0):
            if not head:
                return count
            return 1 + get_len(head.next)
        
        len_LL = get_len(head)
        removal_idx = len_LL - n
        
        cur = head
        while cur:
            if removal_idx == 0:
                head = head.next
                return head
            if removal_idx == 1:
                old_nxt = cur.next
                new_nxt = old_nxt.next
                cur.next = new_nxt
                return head
            removal_idx -= 1
            cur = cur.next
        
        return head