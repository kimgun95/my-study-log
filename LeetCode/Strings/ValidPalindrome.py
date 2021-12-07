class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z':
                answer.append(s[i])
            elif 'A' <= s[i] <= 'Z':
                # 대 -> 소문자 를 원하면 +32
                answer.append(chr(ord(s[i]) + 32))
            elif '0' <= s[i] <= '9':
                answer.append(s[i])
        answer = ''.join(answer)
        length = len(answer)
        for i in range(length // 2):
            if answer[i] != answer[length - i - 1]:
                return False
        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))