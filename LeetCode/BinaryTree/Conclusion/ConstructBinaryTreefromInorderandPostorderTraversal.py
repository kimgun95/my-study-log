# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # TreeNode를 반환해야 함
        if not inorder or not postorder:
            return None
        # 후위 순회 맨 뒤 값이 root임
        root = TreeNode(postorder.pop())
        # 중위 순회에서 root 위치 찾아낸다
        inorderIndex = inorder.index(root.val)

        # 우측 sub tree를 먼저 만들어야 '후위 순회 맨 뒤 값이 root임'을 계속 만족시킴
        root.right = self.buildTree(inorder[inorderIndex + 1:], postorder)
        root.left = self.buildTree(inorder[:inorderIndex], postorder)

        return root