"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', copies={}) -> 'Node':
        """
        (subtract 1 to get the value of the index)
        1: [2, 4]
        2: [1, 3]
        3: [2, 4]
        4: [1, 3]
        
        hashmap to associate nodes with their copies
        if a copy of curr node exists in hashmap, return that to recursive caller. otherwise...
        create a copy of the curr node with empty neighbor list (HOW TO COPY? WILL REASSIGNING TO A NEW VAR BE ENOUGH?)        
        map curr node to copy node inside of hashmap
        for each neighbor of curr node, create a copy of that neighbor (recurse) and append it to copy's neighbor list
        return the copy node
        """
        if not node:
          return node
        if node in copies:
          return copies[node]
        
        copy = Node(node.val)
        copies[node] = copy
        for nei in node.neighbors:
          # DOES IT MATTER IF YOU ADD TO THE COPY IN MAP OR NOT?
          copies[node].neighbors.append(self.cloneGraph(nei, copies))
        
        return copies[node]
        