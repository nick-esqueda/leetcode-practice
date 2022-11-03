/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        /*
            NO CHILDREN:
                just reassign the parent's .left/.right to null.
            ONE CHILD:
                assign the parent's .left/.right to the one child.
            TWO CHILDREN:
                need to find the IOP of the target.
                switch the values of the nodes.
                delete that IOP.
                    that IOP is guaranteed to only have at most 1 child.
        */
        
        return recursiveNoStack(root, key);
    }
    
    public TreeNode recursiveNoStack(TreeNode root, int key) {
        if (root == null) return null;
        
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else { // found the node to delete.
            
            if (root.left == null && root.right == null) { // NO CHILDREN
                return null;
            } else if (root.left != null && root.right != null) { // TWO CHILDREN
                int predecessorVal = getPredecessor(root, root.val);
                deleteNode(root, predecessorVal);
                root.val = predecessorVal;
                return root;
            } else { // ONE CHILD
                return root.left != null ? root.left : root.right;
            }
        }
        
        return root;
    }
    
    int prev;
    boolean found = false;
    
    public int getPredecessor(TreeNode root, int target) {
        // a predecessor is guaranteed to exist on a root with 2 children.
        if (root == null) return 0;
        
        getPredecessor(root.left, target);
        if (this.found) return this.prev;
        
        if (root.val == target) {
            this.found = true;
            return prev;
        } else {
            this.prev = root.val;
        }
        
        getPredecessor(root.right, target);
        if (this.found) return this.prev;
        
        return 0;
    }
}