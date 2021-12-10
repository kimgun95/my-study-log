from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def isFizzBuzz(num):
            if num % 3 == 0 and num % 5 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            else:
                return str(num)
        answer = []
        for i in range(1, n + 1):
            answer.append(isFizzBuzz(i))
        return answer


s = Solution()
print(s.fizzBuzz(15))