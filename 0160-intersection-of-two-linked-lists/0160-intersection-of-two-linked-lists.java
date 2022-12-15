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
        // return set(headA, headB);
        return twoPointerUsingLen(headA, headB);
    }
    
    private ListNode twoPointerUsingLen(ListNode headA, ListNode headB) {
        int lenA = 0;
        int lenB = 0;
        
        ListNode curr1 = headA;
        ListNode curr2 = headB;
        while (curr1 != null || curr2 != null) {
            if (curr1 != null) {
                ++lenA;
                curr1 = curr1.next;
            }
            if (curr2 != null) {
                ++lenB;
                curr2 = curr2.next;
            }
        }
        
        boolean aIsLonger = lenA - lenB > 0;
        curr1 = aIsLonger ? headA : headB;
        int diff = Math.abs(lenA - lenB);
        while (diff > 0 && curr1 != null) {
            curr1 = curr1.next;
            --diff;
        }
        
        curr2 = aIsLonger ? headB : headA;
        while (curr1 != curr2) {
            curr1 = curr1.next;
            curr2 = curr2.next;
        }
        return curr1;
    }
    
    private ListNode set(ListNode headA, ListNode headB) {
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