# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        traverse through tree
        for each node, see if the value == subroot's value
        if it does, go ahead and call a helper function isSameTree, passing in the curr node and subRoot
        if isSameTree returns true, return true of isSubtree
        if not, keep traversing by calling isSubtree on left and right and return the result
        
        isSameTree:
        if there is no node on both trees, return true
        but if there is a node in one tree but not the other, return false
        if at any node, the node in the other tree is not the same value, return false
        return the result of calling isSameTree on left and right nodes of each tree
        """
        
        if not root:
          return
        
        if root.val == subRoot.val:
          if self.isSameTree(root, subRoot):
            return True
          
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
          
        
        
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
          return True
        if not root or not subRoot:
          return False

        if root.val != subRoot.val:
          return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

