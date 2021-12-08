# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 다른 분의 생각도 보고 적는 내 느낌은 역시 이번 문제는 좋지 않다는 것이다
# 근본적으로 이전 node에서 지금 node를 바라보지 않아야 하는 것이 핵심이다
# 그러나 이 해결책은 전혀 그런 것을 신경쓰지 않아도 되는 풀이이다
class Solution:
    def deleteNode(self, node):
        # tail node가 입력값으로 주어지는 일은 없다!
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next