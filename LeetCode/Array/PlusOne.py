from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. 숫자를 str 변환 후 join으로 합침
        number = ''.join(map(str, digits))
        # 2. str형 숫자를 int형 변환 후 +1, 다시 str로 변환
        number = str(int(number) + 1)
        # 3. list를 통해 한글자씩 자르기, map으로 모두 int형 변환
        number = list(map(int, list(number)))
        return number


s = Solution()
print(s.plusOne([1,2,3]))