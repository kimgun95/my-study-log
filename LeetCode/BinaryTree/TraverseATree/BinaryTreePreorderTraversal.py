# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 전위 순회(root-> 왼 -> 오)
        if root is None:
            return []
        answer = []

        def preorder(node):
            answer.append(node.val)
            if node.left is not None:
                preorder(node.left)
            if node.right is not None:
                preorder(node.right)

        preorder(root)
        return answer