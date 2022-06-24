# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        what to do if two lists are not same length?
        what to do if you have remainders?
        
        use a "remainder" boolean var to flag whether or not you should +1 on this current iteration
        if the sum of the two nodes < 10, set remainder to False
        
        if one of the lists cur is None, keep iterating like normal, but use 0 in place of the missing node, 
            and don't iterate that terminated lists pointer forward
        """
        sum_l = ListNode(0)
        rtn = sum_l
        remainder = 0
        cur1, cur2 = l1, l2
        while cur1 or cur2:
            if not cur1:
                cur_sum = cur2.val + remainder
                cur2 = cur2.next
            elif not cur2:
                cur_sum = cur1.val + remainder
                cur1 = cur1.next
            else:
                cur_sum = cur1.val + cur2.val + remainder
                cur1 = cur1.next
                cur2 = cur2.next
                
            if cur_sum >= 10:
                sum_l.next = ListNode(cur_sum - 10)
                remainder = 1
            else:
                sum_l.next = ListNode(cur_sum)
                remainder = 0
                
            sum_l = sum_l.next
        
        if remainder == 1:
            sum_l.next = ListNode(1)
        return rtn.next
