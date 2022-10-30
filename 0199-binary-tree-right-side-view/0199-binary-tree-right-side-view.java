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
    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new ArrayList<>();
        return bft(root);
    }
    
    public List<Integer> bft(TreeNode root) {
        List<Integer> rightSide = new ArrayList<>();
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            int len = q.size();
            
            for (int i = 0; i < len; ++i) {
                TreeNode curr = q.poll(); 
                if (i == 0) rightSide.add(curr.val);

                if (curr.right != null) q.offer(curr.right);
                if (curr.left != null) q.offer(curr.left);
            }
        }
        
        return rightSide;
    }
}