class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        node = self.head
        size = 1
        while node.next is not None:
            node = node.next
            size += 1
        go = size - k
        node = self.head
        while go:
            node = node.next
            go -= 1
        return node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(12)
linked_list.append(34)
linked_list.append(645)

print(linked_list.get_kth_node_from_last(6).data)