class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
            
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)



#v2：
class Solution:       
    def solveSudoku(self, board: List[List[str]]) -> None:
        def fill(pos:int):
            nonlocal valid
            if pos==len(space):
                valid=True
                return
            i,j=space[pos]

            for digit in range(9):
                if line[i][digit]==column[j][digit]==table[i//3][j//3][digit]==False:
                    line[i][digit]=column[j][digit]=table[i//3][j//3][digit]=True
                    board[i][j]=str(digit+1)
                    fill(pos+1)
                    line[i][digit]=column[j][digit]=table[i//3][j//3][digit]=False
                if valid:
                    return
        space=list()
        column=[[False]*9 for _ in range(9)]
        line=[[False]*9 for _ in range(9)]
        table=[[[False]*9 for _ in range(3)] for _ in range(3)]
        valid=False

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    space.append([i,j])
                else:
                    digit=int(board[i][j])-1
                    line[i][digit]=column[j][digit]=table[i//3][j//3][digit]=True
        fill(0)
        


