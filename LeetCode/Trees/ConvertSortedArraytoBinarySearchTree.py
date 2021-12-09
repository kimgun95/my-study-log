# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# array를 tree로 만드는 문제, TreeNode 클래스를 이용해야함
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        # 인자로 받은 array의 중간 값을 root로 설정
        root = TreeNode(nums[mid])
        # array의 중간값 왼/오른쪽을 sortedArrayToBST로 root 설정
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root