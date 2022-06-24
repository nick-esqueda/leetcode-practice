class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}

        # LRU(0,0) <-> MRU(0,0)
        self.LRU = Node(0, 0)
        self.MRU = Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        
    def insert(self, node):
        """
        want to insert at the back/MRU side
        doesn't really matter if it's over cap
            you can deal with that inside the put section
            you can remove() after insert() if it's over cap
        """
        prev = self.MRU.prev
        prev.next = node
        node.prev = prev
        node.next = self.MRU
        self.MRU.prev = node
        
    def remove(self, node):
        """
        remove node from any point in the list
        """
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:
        """
        1. get when key is already the MRU
        2. get when key is the LRU
        3. get when key is in the middle of the LL
        """
        if key in self.cache_map:
            self.remove(self.cache_map[key])
            self.insert(self.cache_map[key])
            return self.cache_map[key].val
        return -1
            
    def put(self, key: int, value: int) -> None:
        """
        1. put when empty
        2. put when under capacity
        3. evict and put new
        """
        node = Node(key, value)
        if key in self.cache_map:
            self.remove(self.cache_map[key])
        self.cache_map[key] = node
        self.insert(self.cache_map[key])
        
        if len(self.cache_map) > self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.cache_map[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)