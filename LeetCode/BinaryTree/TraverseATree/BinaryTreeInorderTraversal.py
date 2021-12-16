# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 중위 순회(왼 -> root -> 오)
        if root is None:
            return []
        answer = []

        def inorder(node):
            if node.left is not None:
                inorder(node.left)
            answer.append(node.val)
            if node.right is not None:
                inorder(node.right)

        inorder(root)
        return answer