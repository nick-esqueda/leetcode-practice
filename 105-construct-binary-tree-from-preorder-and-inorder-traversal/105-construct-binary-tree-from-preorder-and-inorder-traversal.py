# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        NOTES:
        the first value of the preorder list (after popping) is always the root of the left subtree
        
        if preorder or inorder are empty or have 1 item, return
        curr = pop the front of preorder
        find curr's index inside inorder, and save the length of left and right of inorder
          need to split into L and R as well
        split preorder into left and right based on L/R lengths of inorder
        set curr.left to front of preorderL and curr.right to the front of preorderR
          ??? if there's nothing in the left arr, does curr.left = emptyList[0] set it to None or something else?
        buildTree(curr.left) and buildTree(curr.right) and pass in preorder and inorder of corresponding sides
        return curr
        """
        if not preorder or not inorder:
          return None
        
        curr_val = preorder.pop(0)
        root = TreeNode(curr_val)
        
        idx = inorder.index(curr_val)
        inorder_L, inorder_R = inorder[:idx], inorder[idx + 1:]
        preorder_L, preorder_R = preorder[:idx], preorder[idx:]
        
        root.left = self.buildTree(preorder_L, inorder_L)
        root.right = self.buildTree(preorder_R, inorder_R)
        
        return root
      
        # [0, 1, 2, 3]
        # [0, 1, 2, 3]
        
        