class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        minus = 1
        number = 0
        # 1. 맨 앞 공백을 지운다
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        # 2. '+' or '-' 부호를 한 번 처리
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                minus = -1
            idx += 1
        # 3. 숫자만 읽어서 저장
        while idx < len(s) and '0' <= s[idx] <= '9':
            number = 10 * number + int(s[idx])
            idx += 1
        number *= minus
        # 4. int형 범위 밖 수 처리
        if number < -pow(2, 31):
            number = -pow(2, 31)
        elif number >= pow(2, 31):
            number = pow(2, 31) - 1
        return number


s = Solution()
print(s.myAtoi("42"))
print(s.myAtoi("   -42"))
print(s.myAtoi("4193 with words"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))