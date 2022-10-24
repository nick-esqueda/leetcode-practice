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
    private int shortestPath;
    
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        shortestPath = Integer.MAX_VALUE;
        getPathLengths(root, 0);
        return shortestPath;
    }
    
    public void getPathLengths(TreeNode root, int length) {
        if (root == null) return;
        
        ++length;
        if (root.left == null && root.right == null) {
            shortestPath = Math.min(shortestPath, length);
        }
        
        getPathLengths(root.left, length);
        getPathLengths(root.right, length);
    }
}