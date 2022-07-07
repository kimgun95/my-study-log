# Least Recently Used를 구현하는 문제와 다를 바 없다.
def solution(cacheSize, cities):
    answer = 0

    class Node: # 이중 연결 리스트에서 사용할 node 클래스 정의
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    class DoublyLinkedList:
        def __init__(self, cache_size): # 이중 연결 리스트 정의
            self.cache_size = cache_size
            self.head = Node("")
            self.tail = Node("")
            self.head.next = self.tail
            self.tail.prev = self.head

        def LRU(self, data):
            nonlocal answer
            node = self.head.next
            while node.data:
                if node.data == data: # 캐시 안에 데이터가 있다면
                    answer += 1
                    self.cacheHit(node, data)
                    return
                node = node.next
            answer += 5
            self.cacheMiss(data) # 캐시 안에 데이터가 없다면

        def cacheHit(self, node, data):
            self.removeNode(node)
            self.addFront(data)

        def cacheMiss(self, data):
            self.addFront(data)
            if self.totalLen(data) > self.cache_size:
                self.removeBack()

        def removeNode(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def removeBack(self):
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev

        def addFront(self, data):
            newNode = Node(data)
            self.head.next.prev = newNode
            newNode.next = self.head.next
            self.head.next = newNode
            newNode.prev = self.head

        def totalLen(self, data):
            node = self.head.next
            size = 0
            while node.next:
                size += 1
                node = node.next
            return size

    DLL = DoublyLinkedList(cacheSize)
    for city in cities:
        DLL.LRU(city.upper())

    return answer