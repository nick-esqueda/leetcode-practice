/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode front;
    
    public boolean isPalindrome(ListNode head) {
        front = head;
        return _isPalindrome(head);
    }

    private boolean _isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        
        boolean areOuterNodesPalindrome = _isPalindrome(head.next);
        
        if (!areOuterNodesPalindrome || head.val != front.val) {
            return false;
        }
        
        front = front.next;
        return true;
    }
}