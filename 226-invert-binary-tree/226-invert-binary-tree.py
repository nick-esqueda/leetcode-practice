# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        create a queue with the root node inside of it
        while the queue has nodes still on it...
        pop the first node in queue
        save the original root.left and root.right
        reassign root.left to root.right and vice versa
        if they exist, push each left and right children of the node to the queue
        keep looping
        return the root
        """
        
        if not root: return root
        
        q = [root]
        while q:
          node = q.pop(0)
          
          oldLeft = node.left
          node.left = node.right
          node.right = oldLeft
          
          if node.left: q.append(node.left)
          if node.right: q.append(node.right)
        return root
        