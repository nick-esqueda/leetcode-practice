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
    public TreeNode sortedArrayToBST(int[] nums) {
        /*
        PROBLEM:
        input is strictly increasing.
        resulting tree must be height balanced.
        
        THOUGHTS:
        if we have to have it balanced, then...
        well, we know the very middle of the array should be the root.
            - which mid though? left/right mid?
        the left subtree of the root/middle is the whole subarray to the left.
        vice versa for the right.
        so if you recursively take the middle of the array as the root, and bulid 
        the left and right subtrees with either end of the mid, you can get the result.
        does the middle matter? i don't think so, as long as the choice is consistent.
        */
        
        return buildTree(nums, 0, nums.length - 1);
    }
    
    private TreeNode buildTree(int[] nums, int start, int end) { // "end" IS INCLUSIVE.
        if (start > end) { 
            return null;
        }
        
        int mid = (end + start) / 2; // left mid.
        
        TreeNode root = new TreeNode(nums[mid]);
        root.left = buildTree(nums, start, mid - 1);
        root.right = buildTree(nums, mid + 1, end);
        return root;
    }
}