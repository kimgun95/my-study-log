# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 연결 리스트에 대해 많이 생각하게 되는 문제
# time: O(n), space: O(1)을 권장하는데 이 풀이가 O(1)을 만족하는건가?
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # tortoise: 거북이, hare: 토끼 (플로이드 사이클 탐지 알고리즘 참고)
        tortoise, hare = head, head
        # 중간 위치를 찾는다
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
        # 중간 위치 이후 reversed linked list 구현 (이때 중간 값은 next를 None으로 설정)
        prev, cur, prev.next = tortoise, tortoise.next, None
        while cur:
            temp = cur.next
            cur.next, prev, cur = prev, cur, temp
        # while의 조건에 head, tail 둘 중 하나를 넣어야 하는 데 tail값을 넣은 이유
        # 노드의 개수가 짝수일 때 겹치는 중간 값은 없다, 따라서 tail에 가까운 중간값의 next가 위에서 None으로 설정된다
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True