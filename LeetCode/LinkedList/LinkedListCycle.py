# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # None이 있다면 반복문은 종료될 것 -> False 반환
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            # 탐색하다가 node가 겹칠때 종료 -> True 반환
            if slow is fast:
                return True
        return False