# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        the diameter of a tree is the length of the longest path between any two nodes in a tree
          i.e. the nodes that are 'farthest apart'
        the diameter is going to have a parent (doesn't have to be the root)
        if you can calculate the max depth of both left and right subtrees and add those together, THAT is the diameter
        
        create a closure over a variable that keeps track of a maxDiameter
        traverse through tree depth first
        get the height of the left subtree and the right subtree and add them together (diameter)
          if node is null, return a depth of 0
          recurse for left, recurse for right
          add the depth of left + right
          if diameter > maxDiameter, replace maxDiameter
          return the height of this node (the max height of left/right subtrees)
        after the traversal, return maxDiameter
        """
        
        maxDiameter = -1
        
        def dft(node):
          nonlocal maxDiameter
          
          if not node:
            return -1
          
          heightL, heightR = dft(node.left), dft(node.right)
          diameter =  heightL + heightR + 2
          maxDiameter = max(diameter, maxDiameter)
          
          return max(heightL, heightR) + 1
          
        dft(root)
        return maxDiameter