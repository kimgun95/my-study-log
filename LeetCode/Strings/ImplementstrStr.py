class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle, len_haystack = len(needle), len(haystack)
        # 1. needle이 empty라면 0 리턴
        if len_needle == 0:
            return 0
        # 2. haystack이 empty면 -1 리턴
        if len_haystack == 0:
            return -1
        # 3. 구간 마다 문자열 일치하는 곳을 찾음
        for i in range(len_haystack - len_needle + 1):
            # 마지막 테스트 케이스에서 시간 초과 발생
            # 4. 맨 마지막 글자를 확인하는 것이 효율적일 것 같아 코드 추가 -> 시간 초과 해결
            if haystack[i + len_needle - 1] != needle[len_needle - 1]:
                continue
            for j in range(len_needle):
                if haystack[i + j] != needle[j]:
                    break
                if j == len_needle - 1:
                    return i
        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("", ""))
print(s.strStr("aaaab", "aaaab"))