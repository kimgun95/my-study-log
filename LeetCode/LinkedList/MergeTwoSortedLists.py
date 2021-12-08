# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        # 비어있는 연결리스트를 받을 때 처리
        if l1 is None and l2 is None:
            return l1
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        # 첫 노드 설정 (이 노드는 정답 노드가 된다)
        if l1.val > l2.val:
            node, answer = l2, l2
            l2 = l2.next
        else:
            node, answer = l1, l1
            l1 = l1.next
        # list1과 list2 노드를 비교하며 연결
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                node.next = l2
                node = l2
                l2 = l2.next
            else:
                node.next = l1
                node = l1
                l1 = l1.next

        def murge_remainder(remain_node):
            nonlocal node
            node.next = remain_node
            node = remain_node
            if remain_node.next is not None:
                murge_remainder(remain_node.next)

        # 연결하지 않은 노드가 한 쪽 연결리스트에 남아있다면 연결
        if l1 is not None:
            murge_remainder(l1)
        elif l2 is not None:
            murge_remainder(l2)
        return answer