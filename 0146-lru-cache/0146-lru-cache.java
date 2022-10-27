class Node {
    public int key;
    public int val;
    public Node next;
    public Node prev;
    
    public Node(int key, int val) {
        this.key = key; // need the cache key to facilitate eviction.
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    public int count;
    public final int capacity;
    public Map<Integer, Node> cache;
    public Node head;
    public Node tail;

    public LRUCache(int capacity) {
        this.count = 0;
        this.capacity = capacity; // must be >= 1.
        this.cache = new HashMap<>();
        this.head = null;
        this.tail = null;
    }
    
    public int get(int key) {
        /*
        - returns the value of the Node with the key (if exists).
        - moves that Node to the back of the queue (MRU).
        */
        
        if (!this.cache.containsKey(key)) return -1;
        
        Node node = this.cache.get(key);
        removeNode(node);
        enqueue(node);
        
        return node.val;
    }
    
    public void put(int key, int value) {
        /*
        - puts a new node into the LRU cache, or updates the value of an 
        existing Node with the given key.
        - will move that new/modified Node to the back of the queue (MRU).
        - will evict the LRU Node if at capacity.
        */
        
        if (this.cache.containsKey(key)) {
            // UPDATE - if key/Node already exists, remove it from the queue
            // so that it can be updated and put at the back of the queue.
            Node oldNode = this.cache.get(key);
            removeNode(oldNode);
        } else if (this.count == this.capacity) {
            // AT CAPACITY - if capacity is reached, evict the LRU Node 
            // before adding the new one.
            Node LRU = dequeue();
            this.cache.remove(LRU.key);
        }
        
        // PUT - add the Node to the queue and cache.
        Node newNode = new Node(key, value);
        this.cache.put(key, newNode);
        enqueue(newNode);
    }
    
    public void enqueue(Node node) {
        /*
        puts the given node at the end of the queue.
        will increment length.
        (a.k.a. addToTail)
        */
        
        if (this.count == 0) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = this.tail.next;
        }
        
        this.count += 1;
    }
    
    public Node dequeue() {
        /*
        removes the head of the queue and returns it.
        will decrement length.
        (a.k.a. removeFromHead)
        */
        if (this.count == 0) return null;
        
        Node oldHead = this.head;
        this.head = this.head.next;
        if (this.head != null) {
            this.head.prev = null;
        } else {
            this.tail = null;
        }
        
        this.count -= 1;
        return oldHead;
    }

    public Node removeFromTail() {
        /*
        removes the end of the queue and returns it.
        will decrement length.
        (a.k.a. removeFromTail)
        */
        if (this.count == 0) return null;
        
        Node oldTail = this.tail;
        this.tail = this.tail.prev;
        if (this.tail != null) {
            this.tail.next = null;
        } else {
            this.head = null;
        }
        
        this.count -= 1;
        return oldTail;
    }
    
    public void removeNode(Node node) {
        /*
        will remove the given Node from wherever it is in the queue.
        will decrement length.
        */
        if (this.count == 0) return;
        
        if (node == this.head) {
            dequeue();
        } else if (node == this.tail) {
            removeFromTail();
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
            this.count -= 1;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */