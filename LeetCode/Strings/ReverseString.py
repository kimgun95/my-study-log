from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        return


s = Solution()
print(s.reverseString(["h","e","l","l","o"]))