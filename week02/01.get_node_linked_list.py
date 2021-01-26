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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        idx = 0
        cur = self.head
        while index != idx:
            idx += 1
            cur = cur.next
        return cur

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()
print(linked_list.get_node(0).data)