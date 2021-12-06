from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. 행 검사
        for i in range(9):
            stack = []
            for j in range(9):
                if board[i][j] in stack:
                    return False
                elif board[i][j] != '.':
                    stack.append(board[i][j])
        # 2. 열 검사
        for j in range(9):
            stack = []
            for i in range(9):
                if board[i][j] in stack:
                    return False
                elif board[i][j] != '.':
                    stack.append(board[i][j])
        # 3. 구간 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                stack = []
                for y in range(i, i + 3):
                    for x in range(j, j + 3):
                        if board[y][x] in stack:
                            return False
                        elif board[y][x] != '.':
                            stack.append(board[y][x])
        return True


s = Solution()
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))