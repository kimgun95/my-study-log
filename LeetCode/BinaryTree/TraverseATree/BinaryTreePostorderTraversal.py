# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 후위 순회(왼 -> 오 -> root)
        if root is None:
            return []
        answer = []

        def postorder(node):
            if node.left is not None:
                postorder(node.left)
            if node.right is not None:
                postorder(node.right)
            answer.append(node.val)

        postorder(root)
        return answer