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


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!