class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sort_s, sort_t = list(s), list(t)
        sort_s.sort()
        sort_t.sort()
        for i in range(len(s)):
            if sort_s[i] != sort_t[i]:
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))