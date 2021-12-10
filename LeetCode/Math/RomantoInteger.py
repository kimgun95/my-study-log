class Solution:
    def romanToInt(self, s: str) -> int:
        def toInt(word):
            if word == 'I':
                return 1
            elif word == 'V':
                return 5
            elif word == 'X':
                return 10
            elif word == 'L':
                return 50
            elif word == 'C':
                return 100
            elif word == 'D':
                return 500
            elif word == 'M':
                return 1000
        answer = 0
        words = list(s)
        idx = 0
        while idx < len(words):
            if words[idx] == 'I':
                if idx + 1 < len(words) and (words[idx + 1] == 'V' or words[idx + 1] == 'X'):
                    answer += (toInt(words[idx + 1]) - toInt(words[idx]))
                    idx += 2
                    continue
            if words[idx] == 'X':
                if idx + 1 < len(words) and (words[idx + 1] == 'L' or words[idx + 1] == 'C'):
                    answer += (toInt(words[idx + 1]) - toInt(words[idx]))
                    idx += 2
                    continue
            if words[idx] == 'C':
                if idx + 1 < len(words) and (words[idx + 1] == 'D' or words[idx + 1] == 'M'):
                    answer += (toInt(words[idx + 1]) - toInt(words[idx]))
                    idx += 2
                    continue
            answer += toInt(words[idx])
            idx += 1
        return answer


s = Solution()
print(s.romanToInt("MCMXCIV"))