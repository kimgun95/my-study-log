class Solution:
    def countAndSay(self, n: int) -> str:
        # 내 코드가 살짝 길어서 깔끔한 것을 가져옴(원래 코드도 통과함)
        start = "1"
        for i in range(2, n + 1):
            count = 0
            curr = start[0]
            result = ""
            for char in start:
                if char == curr:
                    count += 1
                elif char != curr:
                    # 문자열을 이런식으로 더해서 추가할 수 있음
                    result += str(count) + curr
                    count = 1
                    curr = char
            result += str(count) + curr
            start = result

        return start


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(4))