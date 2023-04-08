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
        // get the length of the list so that we can split it in half.
        int listLength = getListLength(head);
        // if list only has one element, it is a palindrome.
        if (listLength == 1) {
            return true;
        }

        // split the list in half, and get the head of each half.
        ListNode[] listHalves = splitListInHalf(head, listLength);
        ListNode firstHalf = listHalves[0];
        ListNode secondHalf = listHalves[1];
        
        // now that the two lists are disconnected, reverse one half in-place.
        ListNode firstHalfReversed = reverseLinkedListInPlace(firstHalf);
        
        // iterate through both lists and check equality on each step through. 
        // based on this, return the boolean.
        return areListsSame(firstHalfReversed, secondHalf);
    }
    
    public boolean areListsSame(ListNode headA, ListNode headB) {
        ListNode currentA = headA;
        ListNode currentB = headB;
        
        while ((currentA != null) && (currentB != null)) {
            if (currentA.val != currentB.val) {
                return false;
            }
            
            currentA = currentA.next;
            currentB = currentB.next;
        }
        
        return true;
    }

    
    public ListNode reverseLinkedListInPlace(ListNode head) {        
        ListNode currentNode = head;
        ListNode previousNode = null;
        while (currentNode != null) {
            ListNode nextNode = currentNode.next;
            
            currentNode.next = previousNode;
            previousNode = currentNode;
            currentNode = nextNode;
        }
        
        return previousNode;
    }
        
    public ListNode[] splitListInHalf(ListNode head, int listLength) {
        int index = 0;
        int halfwayPoint = listLength / 2; // floor/integer division
        ListNode previousNode = null;
        ListNode currentNode = head;
        while (index < halfwayPoint) {
            previousNode = currentNode;
            currentNode = currentNode.next;
            index += 1;
        }

        // if odd length, then you can exclude the middle node.
        if (listLength % 2 == 1) {
            currentNode = currentNode.next;
        }

        previousNode.next = null; // disconnect the two lists.

        return new ListNode[] { head, currentNode };
    }
    
    public int getListLength(ListNode head) {
        int listLength = 0;
        ListNode currentNode = head;
        while (currentNode != null) {
            listLength += 1;
            currentNode = currentNode.next;
        }
        
        return listLength;
    }

}