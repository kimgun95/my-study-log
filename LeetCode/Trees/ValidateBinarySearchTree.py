# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 함수 인자로 left, right 값을 넣어야 겠다는 생각을 못함...ㅠ
        # 초기 root의 low, high값도 아이디어가 좋은 것 같음
        def isValid(node, low, high):
            if node is None:
                return True
            elif not low < node.val < high:
                return False
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
        return isValid(root, low=float('-inf'), high=float('inf'))