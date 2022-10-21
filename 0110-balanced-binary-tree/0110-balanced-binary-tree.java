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
    private boolean globalBalanced;
    
    public boolean isBalanced(TreeNode root) {
        globalBalanced = true;
        compareHeights(root);
        return globalBalanced;
    }
    
    public int compareHeights(TreeNode root) {
        if (root == null) return -1;
        
        int leftHeight = compareHeights(root.left);
        int rightHeight = compareHeights(root.right);
        
        if (Math.abs(leftHeight - rightHeight) > 1) {
            globalBalanced = false;
        }
        
        return 1 + Math.max(leftHeight, rightHeight);
    }
}





