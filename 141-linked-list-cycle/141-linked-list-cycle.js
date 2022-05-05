/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  /*
    **ASSUME EVERY NODE'S VALUE IN LL ARE UNIQUE
    

    create a set to store all of the values of nodes that i've visited
    start iterating through the LL starting at head
    if you come across a node that has null as next, return false
    check if the curr node's value is inside the set. if it isn't, add it to the set, otherwise return true
  */
  
  if (!head) return false;
  
  let currNode = head;
  while (currNode.next) {
    if (currNode['hello'] === 'hello') return true;
    else currNode['hello'] = 'hello';
      
    currNode = currNode.next;
  }
  
  return false;
};

// [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
// -1