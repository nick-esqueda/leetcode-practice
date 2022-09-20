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
    private int maxDiameter;
    
    public int diameterOfBinaryTree(TreeNode root) {
        /*
            get the length of the max node-to-leaf path in the left and right subtrees.
            add them together to get the diameter using that node as the "break point".
            compare to a global maximum and reassign if a new max is found.
        */
        maxDiameter = 0;
        findDiameter(root);
        return maxDiameter;
    }
    
    public int findDiameter(TreeNode root) {
        if (root == null) return -1;
        
        int leftLen = 1 + findDiameter(root.left);
        int rightLen = 1 + findDiameter(root.right);
        
        maxDiameter = Math.max(maxDiameter, leftLen + rightLen);
        return Math.max(leftLen, rightLen);
    }
}