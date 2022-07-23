# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        
        PRE-ORDER DFS
        """
        serialized = []
        def dfs(root):
            if not root:
                serialized.append('N')
                return
            
            serialized.append(f"{root.val}")
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(serialized)
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
                1           
              /   \             
             2     3         
            / \   / \           
           4   5  6  7
          / \
         8   9
        
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
         0  1  2  3  4  5  6  7  8
        
        left child = i*2 + 1
        right child = i*2 + 2
        """
        if len(data) == 0:
            return
        
        data = data.split(',')
        i = 0
        def build_tree():
            nonlocal i
            if i == len(data):
                return None
            if data[i] == "N":
                data.pop(0)
                return None
            
            root = TreeNode(int(data[i]))
            i += 1
            root.left = build_tree()
            root.right = build_tree()
            return root
        
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))