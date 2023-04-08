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
    public boolean isPalindrome(ListNode head) {
        List<Integer> orderedListValues = new ArrayList<>();
        
        // collect node values in an ordered list.
        ListNode currentNode = head;
        while (currentNode != null) {
            orderedListValues.add(currentNode.val);
            currentNode = currentNode.next;
        }

        // iterate over linked list forwards, iterate over ordered list backwards,
        // if not equal during an iteration, then list is not palindrome.
        currentNode = head;
        for (int i = orderedListValues.size() - 1; i >= 0; --i) {
            int val1 = orderedListValues.get(i);
            int val2 = currentNode.val;
            
            if (val1 != val2) {
                return false;
            }
            
            currentNode = currentNode.next;
        }
        
        return true;
    }
}