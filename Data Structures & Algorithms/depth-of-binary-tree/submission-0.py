# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0
        queue.append(root)
        if root is None:
            return 0
        while queue:
            nodes_in_level = len(queue)
            for neighbour in range(nodes_in_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
#                if neighbour not in queue:
#                    queue.append(neighbour)

        return level
        