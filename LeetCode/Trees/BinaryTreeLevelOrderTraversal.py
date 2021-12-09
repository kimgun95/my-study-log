# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def search(node, depth):
            if node is None:
                return
            if depth > len(answer):
                answer.append([node.val])
            else:
                answer[depth].append(node.val)
            search(node.left, depth + 1)
            search(node.right, depth + 1)
            return

        search(root, 0)
        return answer
