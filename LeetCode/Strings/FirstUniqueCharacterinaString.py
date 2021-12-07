class Solution:
    def firstUniqChar(self, s: str) -> int:
        # dp로 생각해서 run time을 줄임(카운트 한 번 실행한 알파벳은 저장)
        dic = dict()
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = s.count(s[i])
                if dic[s[i]] == 1:
                    return i
            else:
                continue
        return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar("aabb"))