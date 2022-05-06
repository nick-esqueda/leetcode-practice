/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */



var mergeTwoLists = function(list1, list2) {
  class Bruh {
    constructor(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
    }
  }
  
  // idk
  
  const resList = new Bruh(0, null);
  let resTail = resList;
  
  let curr1 = list1;
  let curr2 = list2;
  
  while (curr1 && curr2) {
    if (curr1.val < curr2.val) {
      resTail.next = curr1;
      curr1 = curr1.next;
      resTail = resTail.next;      
    } else if (curr1.val >= curr2.val) {
      resTail.next = curr2;
      curr2 = curr2.next;
      resTail = resTail.next;
    }
  }
  
  if (curr1) {
    resTail.next = curr1;
  } else if (curr2) {
    resTail.next = curr2;
  }
  
  return resList.next;
};