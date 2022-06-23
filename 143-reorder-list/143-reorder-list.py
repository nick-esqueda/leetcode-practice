# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        find the midpoint of the list using a slow and fast pointer
        save the 2nd half of the list (can set the midpoint's .next = None)
        reverse the 2nd half of the list
        zipper the two lists together
        
        FINDING MIDPOINT:
        set slow to head, fast to head.next
        move up fast by 2, slow by 1
        EVEN LL: fast.next will be None, slow will be the left of the midpoint (mid is between 2 nodes)
            1 -> 2 -|> 3 -> 4 -> N
        ODD LL: fast will be None, slow will be exact midpoint
            1 -> 2 -> |3 -> 4 -> 5 -> N
            
        REVERSE BACK HALF:
        set prev = None
        save next to a var
        set cur.next to prev
        move cur and prev up
        
        ZIPPER:
        start with the head
        save head.next
        save back_half.next
        set head.next to front of back_half
        set back_half.next to the former head.next
        move the pointers up
        idk, something like this
        """
        # FIND MIDPOINT
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        back = slow.next
        slow.next = None
        
        # REVERSE BACK HALF
        cur, prev = back, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # ZIPPER FRONT AND BACK HALVES
        front, back = head, prev
        while front and back:
            front_nxt = front.next
            back_nxt = back.next
            
            front.next = back
            back.next = front_nxt
            
            front = front_nxt
            back = back_nxt

        return front