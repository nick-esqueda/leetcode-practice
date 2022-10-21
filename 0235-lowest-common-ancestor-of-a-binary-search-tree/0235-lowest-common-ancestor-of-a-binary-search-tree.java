/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    private TreeNode LCA;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        LCA = new TreeNode();
        findLCA(root, p, q);
        return LCA;
    }
    
    public boolean findLCA(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return false;
        
        boolean isRoot = root.val == p.val || root.val == q.val;
        boolean inLeft = findLCA(root.left, p, q);
        boolean inRight = findLCA(root.right, p, q);
        
        if ((inLeft && inRight) || (isRoot && inLeft) || (isRoot && inRight)) {
            LCA = root;
        } else if (isRoot || inLeft || inRight) {
            return true;
        }
        
        return false;
    }
}