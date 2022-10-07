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
        
        getPreOrder(root, preOrder);
        return preOrder;
    }
    
    public void getPreOrder(Node root, List<Integer> ordering) {
        ordering.add(root.val);
        for (Node nei: root.children) {
            getPreOrder(nei, ordering);
        }
    }
}