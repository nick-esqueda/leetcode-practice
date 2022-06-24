# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        """
        dummy = ListNode(0)
        curd = dummy
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                curd.next = cur1
                curd = curd.next
                cur1 = cur1.next
            else:
                curd.next = cur2
                curd = curd.next
                cur2 = cur2.next
                
        if cur1:
            curd.next = cur1
        elif cur2:
            curd.next = cur2
        
        return dummy.next