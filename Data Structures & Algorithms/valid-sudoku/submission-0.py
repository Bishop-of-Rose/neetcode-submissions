class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        columns = []
        squares = []

        for i in range(9):
            rows.append(set())
            columns.append(set())
            squares.append(set()) 

        for i in range(len(board)):
            for j in range(len(board[i])):
                current = {board[i][j]}
                current_row = rows[i]
                current_column = columns[j]
                current_square = squares[3 * (i // 3) + j // 3]

                if current != {'.'}:
                    print
                    nunique_row = not (current_row.isdisjoint(current))
                    nunique_column = not (current_column.isdisjoint(current))
                    nunique_square = not (current_square.isdisjoint(current))
                    nunique = nunique_row | nunique_column | nunique_square

                    if nunique:
                        print(current_row, current_column, current_square, i, j)
                        return False

                    current_row |= current
                    current_column |= current
                    current_square |= current
                
        return True
                    

        