from heapq import heapify, heappop, heappush

class Solution:
    def print_board(self, board: list[list[str]]) -> None:
        for rowIdx, row in enumerate(board):
            if rowIdx != 0 and rowIdx % 3 == 0:
                print("#" * 23)
            for colIdx, cell in enumerate(row):
                if colIdx != 0 and colIdx % 3 == 0:
                    print("#", end=" ")
                print(cell, end=" ")
            print()
        print()

    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [ set() for _ in range(9) ]
        cols = [ set() for _ in range(9) ]
        grids = [ [set() for _ in range(3) ] for _ in range(3) ]
        empty_cells = []
        for rowIdx, row in enumerate(board):
            for colIdx, val in enumerate(row):
                if val == ".":
                    empty_cells.append((rowIdx, colIdx))
                else:
                    rows[rowIdx].add(val)
                    cols[colIdx].add(val)
                    grids[rowIdx // 3][colIdx // 3].add(val)
        empty_cells = [
            (9 - len(rows[rowIdx] | cols[colIdx] | grids[rowIdx // 3][colIdx // 3]), rowIdx, colIdx) # number of possible values at position (rowIdx, colIdx)
            for rowIdx, colIdx in empty_cells
        ]
        heapify(empty_cells)

        def fill_board():
            if not empty_cells:
                return True # board is full
            _, rowIdx, colIdx = heappop(empty_cells)
            row = rows[rowIdx]
            col = cols[colIdx]
            grid = grids[rowIdx // 3][colIdx // 3]
            potential_nums = 0
            for val in "123456789":
                if val in row or val in col or val in grid:
                    continue
                board[rowIdx][colIdx] = val
                row.add(val)
                col.add(val)
                grid.add(val)

                if fill_board():
                    return True
                
                row.remove(val)
                col.remove(val)
                grid.remove(val)
                potential_nums += 1
            heappush(empty_cells, (potential_nums, rowIdx, colIdx))
            return False
    
        fill_board()

if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(s.solveSudoku(board))
    s.print_board(board)
    print()
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    s.print_board(board)
    s.solveSudoku(board)
    s.print_board(board)