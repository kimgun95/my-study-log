# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결 리스트가 비었거나 하나 일 때 그대로 리턴
        if head is None or head.next is None:
            return head
        # 두 번째 node를 기준으로 초기값 설정
        cur_node = head.next
        bef_node, bef_node.next = head, None
        nex_node = head # 세팅이 필요 없어 임의로 초기화만
        while cur_node:
            nex_node = cur_node.next
            cur_node.next = bef_node
            bef_node = cur_node
            cur_node = nex_node
        # 기존의 마지막 node를 반환하면 거꾸로 연결된 연결 리스트로 반환됨
        return bef_node