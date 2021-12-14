import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.list = nums
        return

    def reset(self) -> List[int]:
        return self.list

    def shuffle(self) -> List[int]:
        # 1. 숫자를 하나씩 랜덤하게 뽑아 추가한 나의 풀이
        # answer = []
        # data = [*self.list]
        # while data:
        #     answer.append(data.pop(random.randrange(0, len(data))))
        # return answer
        # 2. random.sample()를 이용한 더 간단한 풀이
        return random.sample(self.list, len(self.list))


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
print(obj.reset())
print(obj.shuffle())