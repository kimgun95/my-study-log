# 파스칼의 삼각형
# 기본 이진트리 보다 구현이 쉬운것 같다
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1] * i for i in range(1, numRows + 1)]
        if numRows < 3:
            return lst
        for depth in range(2, numRows):
            for idx in range(1, len(lst[depth]) - 1):
                lst[depth][idx] = lst[depth - 1][idx - 1] + lst[depth - 1][idx]
        return lst