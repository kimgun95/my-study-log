from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 알 수 없었던 조건: 무조건 맨 앞부터 공통된 문자열을 찾아야 함
        # 이것 때문에 문제 도전 자체를 못했음, 다 비교해야 하는 줄 알고
        prefix = ''
        if len(strs) == 0:
            return prefix
        # 길이가 제일 짧은 걸 비교 prefix로 잡으면 효율적이지 않을까? (추측)
        strs.sort(key=lambda x: len(x))
        prefix = strs[0]
        for i in range(1, len(strs)):
            # 무조건 find시 0 index에서 같아야 함
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if len(prefix) == 0:
                    return prefix
        return prefix


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))