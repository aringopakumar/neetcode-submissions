class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #First condition (row)
        for subLists in board:
            rowMap = {}
            for num in subLists:
                if num != '.' and num in rowMap:
                    return False
                elif num not in rowMap:
                    rowMap[num] = 0

        #Second condition (col)
        for index in range(9):
            colMap = {}
            for boardList in range(9):
                if board[boardList][index] != '.' and board[boardList][index] in colMap:
                    return False
                elif board[boardList][index] not in colMap:
                    colMap[board[boardList][index]] = 0
        
        #Third condition
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                gridMap = {}

                for i in range(3):
                    for j in range(3):
                        value = board[start_row + i][start_col + j]

                        if value == ".":
                            continue
                        if value in gridMap:
                            return False

                        gridMap[value] = 0
        
        return True


                
