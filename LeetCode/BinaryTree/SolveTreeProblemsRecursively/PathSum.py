# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        answer = False

        def dfs(node, value):
            if node is None:
                return
            if node.left is None and node.right is None:
                if value + node.val == targetSum:
                    nonlocal answer
                    answer = True
                return
            dfs(node.left, value + node.val)
            dfs(node.right, value + node.val)
            return

        dfs(root, 0)
        return answer