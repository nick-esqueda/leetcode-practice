/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> preOrder = new ArrayList<>();
        if (root == null) return preOrder;
        
        // getPreOrderRecursive(root, preOrder);
        getPreOrderIterative(root, preOrder);
        return preOrder;
    }
    
    public void getPreOrderIterative(Node root, List<Integer> ordering) {
        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);
        
        while (!stack.isEmpty()) {
            Node curr = stack.pop();
            ordering.add(curr.val);
            
            for (int i = curr.children.size() - 1; i >= 0; --i) {
                stack.push(curr.children.get(i));
            }
        }
    }
    
    public void getPreOrderRecursive(Node root, List<Integer> ordering) {
        ordering.add(root.val);
        for (Node child: root.children) {
            getPreOrderRecursive(child, ordering);
        }
    }
}