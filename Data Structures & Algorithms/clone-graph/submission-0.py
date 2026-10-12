"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtoNew={}
        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]
            copy = Node()
            copy.val = node.val
            oldtoNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        if node is None:
            return None
        else:
            return dfs(node)
        