# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        None nodes will return up the max path sum of 0
        4 will return up the max path sum of 0 plus itself (4)
            
            2 has 4 in it's left
            goes down to get 6
            we already know MPS is 5
        
        2 has 4 in left and 5 in right
        says "if i were to include myself in this path, the MPS could be 11", but, that would be the whole path
            you have to account for still going up and treating THIS as another path
        so 2 also says, "well 5 is the greater of my children, so i can add myself to 5 and get 7, and this could be part of another path"
        
        so, if you decide to terminate a path (by including current node in the sum), reassign your max path variable, but only return up the other sum
        
        POST ORDER, since need both children to determine MPS
        """
        
        mps = float('-inf')
        
        def find_max_path(root):
            nonlocal mps
            if not root:
                return 0
            
            left_no_split = find_max_path(root.left)
            right_no_split = find_max_path(root.right)
            left_no_split = max(left_no_split, 0)
            right_no_split = max(right_no_split, 0)
            
            cur_no_split = root.val + max(left_no_split, right_no_split)
            
            full_path = left_no_split + root.val + right_no_split
            
            mps = max(mps, full_path)
            return cur_no_split
        
        root_no_split = find_max_path(root)
        return max(mps, root_no_split)