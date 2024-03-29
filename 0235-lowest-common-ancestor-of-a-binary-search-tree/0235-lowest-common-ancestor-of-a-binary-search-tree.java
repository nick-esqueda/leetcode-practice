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
        return findLCABST(root, p, q);
        
        // LCA = new TreeNode();
        // findLCABT(root, p, q);
        // findLCABST(root, p, q);
        // return LCA;
    }
    
    public boolean findLCABT(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return false;
        
        boolean isRoot = root.val == p.val || root.val == q.val;
        boolean inLeft = findLCABT(root.left, p, q);
        boolean inRight = findLCABT(root.right, p, q);
        
        if ((inLeft && inRight) || (isRoot && inLeft) || (isRoot && inRight)) {
            LCA = root;
        } else if (isRoot || inLeft || inRight) {
            return true;
        }
        
        return false;
    }
    
    public TreeNode findLCABST(TreeNode root, TreeNode p, TreeNode q) {
        if ((p.val <= root.val && q.val >= root.val) || 
            (q.val <= root.val && p.val >= root.val)) {
            return root;
        } else if (p.val < root.val && q.val < root.val) {
            return findLCABST(root.left, p, q);
        } else {
            return findLCABST(root.right, p, q);
        }
    }
}