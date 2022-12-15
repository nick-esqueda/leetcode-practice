/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        return bruteForce(headA, headB);
    }
    
    private ListNode bruteForce(ListNode headA, ListNode headB) {
        /*
        for each node in listA, traverse through listB to see if a node matches.
        */
        
        ListNode currA = headA;
        
        while (currA != null) {
            ListNode currB = headB;
            while (currB != null) {
                if (currB == currA) {
                    return currB;
                }
                currB = currB.next;
            }
            
            currA = currA.next;
        }
        
        return null;
    }
}