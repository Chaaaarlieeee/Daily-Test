#v1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0]*9 for _ in range(9)]
        column = [[0]*9 for _ in range(9)]
        table = [[[0]*9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    digit=int(board[i][j])-1
                    row[i][digit]+=1
                    column[j][digit]+=1
                    table[i//3][j//3][digit]+=1

        for i in range(9):
            for j in range(9):
                if row[i][j]>=2:
                    return False
                if column[i][j]>=2:
                    return False

        for i in range(3):
            for j in range(3):
                for k in range(9):
                    if table[i][j][k]>=2:
                        return False
        return True

