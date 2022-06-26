# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        each item in the list is the head of a linked list
        since you're at the beginning of the list, each of nodes are the min nodes
        if you take all of those nodes and heapify the values, you'll end up with the min of the k group
        you can heapreplace the min with the next value from that same LL, so that the heap is still storing all the min values
        after using the next val, you have to increment the pointer up to the next node in that list
        then, create a node with the popped min and set it to the .next of the merged list
        do all of this again until there are no nodes left
        when at the end of a list, node is None, so need to make sure you don't do anything with a list if cur is None
        
        BUILD K HEAP:
        as you go through each list in order to get all the head values for the initial heap:
            create a dummy node for the list in that index, and assign dummy.next to the whole list
                - this way, you can just perform a deletion on the dummy.next every time you pull from the list
            save the first node's value along with the index k in a tuple
                - this way, you can tell where the node came from in order to get the next node in that specific list
            put that tuple in what will soon be the min-heap []
            delete dummy.next
            
        GETTING/DELETING FROM HEADS:
        you'll want to delete dummy.next
        IF there is a dummy.next...
        save the val of dummy.next so you can return it
        save dummy.next.next
        assign dummy.next to that next next
        
        PUSHING TO MERGED / UPDATING THE HEAP:
        while the heap still has items in it:
            heappop and unpack the val and the k index
            create a new node with val and add it to merged.next
            go to the k index in 'lists' and pull the next val and delete that node
                * this should be done with a helper func that returns None if there are no nodes left
            if there are no nodes left, do nothing
            if a node is returned from the helper:
                save the val with the k index in a tuple
                heappush the tuple to the heap
                
        MERGED LIST:
        create a dummy node as the head of your new merged list
        also need a pointer to iterate along the merged list to add to tail
        to add to list, set cur.next = node you created
        return dummy.next
        
        ???
        how to do this in place?
        """
        def ll_dq(dummy):
            if dummy.next is None:
                return None
            val = dummy.next.val
            nxt = dummy.next.next
            dummy.next = nxt
            return val
        
        min_heap = []
        for k, ll in enumerate(lists):
            if ll:
                dummy = ListNode()
                dummy.next = ll
                lists[k] = dummy
                val = ll_dq(lists[k])
                min_heap.append((val, k))
        heapq.heapify(min_heap)
            
        m_dummy = ListNode()
        cur = m_dummy
        while min_heap:
            val, k = heapq.heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next
            
            val = ll_dq(lists[k])
            if val is not None:
                heapq.heappush(min_heap, (val, k))
                
        return m_dummy.next if m_dummy.next else None
        
