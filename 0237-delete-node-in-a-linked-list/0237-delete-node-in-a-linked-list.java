/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    ListNode prev;
    
    public void deleteNode(ListNode node) {
        /*
        if you reassign each node's val to the node after it,
        then the node will be "deleted".
        to take care of the tail node, keep track of a prev node.
        that way, when you're at the tail node, you can reassign
        prev.next to be null, instead of the current node.
        */
        
        if (node.next == null) {
            prev.next = null;
            return;
        }
        
        node.val = node.next.val;
        prev = node;
        deleteNode(node.next);
    }
}