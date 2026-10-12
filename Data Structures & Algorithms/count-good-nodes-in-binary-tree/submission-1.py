# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return
        max_value = root.val
        def dfs(node,max_value):
            if node is None:
                return 0
            new_max_value = max_value
            if node.val >= max_value :
                current_good = 1
                new_max_value = max(max_value,node.val)
            else:
                current_good = 0
            left = dfs(node.left,new_max_value)
            right = dfs(node.right,new_max_value)
            return current_good+left+right
        return dfs(root,max_value)

        