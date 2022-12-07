/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;
        
        Map<Node, Node> nodeMap = new HashMap<>();
        return clone(node, nodeMap);
    }
    
    public Node clone(Node node, Map<Node, Node> nodeMap) {
        if (nodeMap.containsKey(node)) return nodeMap.get(node);
        
        Node newNode = new Node(node.val);
        nodeMap.put(node, newNode);
        
        List<Node> newNeighbors = new ArrayList<>();
        for (Node nei : node.neighbors) {
            Node newNei = clone(nei, nodeMap);
            newNode.neighbors.add(newNei);
        }
        
        return newNode;
    }
}