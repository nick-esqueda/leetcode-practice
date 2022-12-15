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
        // return bruteForce(headA, headB);
        return set(headA, headB);
    }
    
    private ListNode set(ListNode headA, ListNode headB) {
        /*
        how can we do this in not n^2 time?
        put nodes inside of a set maybe? but, need to verify that the set will 
        operate on memory addresses, not just object properties.
        */
        
        Set<ListNode> setB = new HashSet<>();
        
        // put all listB nodes inside of setB.
        ListNode currB = headB;
        while (currB != null) {
            setB.add(currB);
            currB = currB.next;
        }
        
        // traverse through listA, checking to see if a node exists in setB.
        // if so, return that node, because it is the intersection.
        ListNode currA = headA;
        while (currA != null) {
            if (setB.contains(currA)) {
                return currA;
            }
            currA = currA.next;
        }
        
        return null;
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