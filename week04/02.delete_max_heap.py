class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 새노드 추가
        self.items.append(value)
        cur_idx = len(self.items) - 1

        # root 노드까지 반복
        while cur_idx > 1:
            parent_idx = cur_idx // 2
            # 새노드가 부모보다 크다면 swap
            if self.items[cur_idx] > self.items[parent_idx]:
                self.items[cur_idx], self.items[parent_idx] = self.items[parent_idx], self.items[cur_idx]
                cur_idx = parent_idx
            else:
                break
        return

    def delete(self):
        # root와 맨 뒤 노드를 swap
        self.items[1], self.items[-1] = self.items[-1], self.items[1]

        # 맨 뒤 노드 delete
        delete_val = self.items.pop()
        cur_idx = 1

        # 제일 깊은 깊이까지 반복
        while cur_idx < len(self.items) - 1:
            child_idx = cur_idx * 2 if self.items[cur_idx * 2] > self.items[cur_idx * 2 + 1] else cur_idx * 2 + 1
            # 자식 노드가 부모 노드보다 크다면 swap
            if self.items[cur_idx] < self.items[child_idx]:
                self.items[cur_idx], self.items[child_idx] = self.items[child_idx], self.items[cur_idx]
                cur_idx = child_idx
            else:
                break
        return delete_val  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]