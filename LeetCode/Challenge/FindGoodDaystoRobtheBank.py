from typing import List


# '시간초과' 발생 코드: 수정 필요
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        def isDecrease(idx, depth):
            if depth == time:
                return True
            if security[idx] >= security[idx + 1]:
                return isDecrease(idx - 1, depth + 1)
            return False

        def isIncrease(idx, depth):
            if depth == time:
                return True
            if security[idx] >= security[idx - 1]:
                return isIncrease(idx + 1, depth + 1)
            return False

        answer = []
        for i in range(time, len(security) - time):
            if isDecrease(i - 1, 0) and isIncrease(i + 1, 0):
                answer.append(i)
        return answer


s = Solution
print(s.goodDaysToRobBank(s, [5,3,3,3,5,6,2], 2))
print(s.goodDaysToRobBank(s, [1,1,1,1,1], 0))
print(s.goodDaysToRobBank(s, [1,2,3,4,5,6], 2))
print(s.goodDaysToRobBank(s, [1], 5))