def solution(cacheSize, cities):
    answer = 0

    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    class DoublyLinkedList:
        def __init__(self, cache_size):
            self.cache_size = cache_size
            self.head = Node("")
            self.tail = Node("")
            self.head.next = self.tail
            self.tail.prev = self.head

        def LRU(self, data):
            node = self.head.next
            while node.data:
                if node.data == data:
                    self.cacheHit(node, data)
                    return
                node = node.next
            self.cacheMiss(data)

        def cacheHit(self, node, data):
            newNode = Node(data)
            self.


        def cacheMiss(self, data):

    DLL = DoublyLinkedList(cacheSize)
    for city in cities:


    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
