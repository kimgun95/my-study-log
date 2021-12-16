from typing import List

# ex)  matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotate가 행reverse -> 대각선reverse로 해결할 수 있다는 아이디어...가 중요했다
# in-place하게 정렬을 하는 것은 reverse로 생각을 하는게 좋은 것 같다
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        down = len(matrix) - 1
        # 행 기준 reverse matrix 변환
        while top < down:
            temp = matrix[top]
            matrix[top] = matrix[down]
            matrix[down] = temp
            top += 1
            down -= 1
        # 대각선 기준 reverse 변환
        for i in range(len(matrix) - 1):
            for j in range(i + 1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp


s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))