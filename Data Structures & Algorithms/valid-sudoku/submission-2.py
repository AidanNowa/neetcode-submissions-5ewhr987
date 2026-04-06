class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:      
        transposed = [[row[i] for row in board] for i in range(len(board[0]))]

        #check rows
        for row in board:
            seen = set()
            for val in row:
                if val == '.':
                    continue
                if val in seen:
                    print(f'bad row: {row}')
                    return False
                seen.add(val)
        #check columns
        for row in transposed:
            seen = set()
            for val in row:
                if val == '.':
                    continue
                if val in seen:
                    print(f'bad col: {row}')
                    return False
                seen.add(val)
        #check squares
        row_len = len(board[0])
        col_len = len(board)
        squares = [[0 for _ in range(9)] for _ in range(9)]
        #squares 1-3
        for i in range(0, 3):
            for j in range(0, col_len):
                squares_index = (i//3) + (j//3)
                if board[i][j] == '.':
                    continue
                else:
                    squares[squares_index][int(board[i][j]) - 1] += 1
        #squares 4-6
        for i in range(3, 6):
            for j in range(0, col_len):
                squares_index = (i//3) + (j//3) + 2
                if board[i][j] == '.':
                    continue
                else:
                    # print(f"s_index: {squares_index}")
                    squares[squares_index][int(board[i][j]) - 1] += 1
        #squares 7-9
        for i in range(6, 9):
            for j in range(0, col_len):
                squares_index = (i//3) + (j//3) + 4
                if board[i][j] == '.':
                    continue
                else:
                    # print(f"s_index: {squares_index}")
                    squares[squares_index][int(board[i][j]) - 1] += 1
 
        # for i in range(len(board)):
            # print(f"{i}: {board[i]}")
        # for row in squares:
            # print(row)
        for row in squares:
            if 2 in row:
                return False
        
        return True
        