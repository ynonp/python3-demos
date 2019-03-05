def scan_board(board, code_to_run_for_each_item, code_to_run_for_each_row):
    for i in range(len(board)):
        for j in range(len(board[i])):
            res = code_to_run_for_each_item(i, j)
            if res is not None:
                return res

        code_to_run_for_each_row()

class HumanPlayer:
    def next_move(self, board):
        self.print_board(board)
        next_move = input("What's your next move? type the square position as (row, column)")
        return next_move

    def print_board(self, board):
        scan_board(
            board,
            lambda i, j: print(f"{board[i][j]:3}", end=""),
            lambda: print()
        )


class AIPlayer:
    def next_move(self, board):
        def foreach_cell(i, j):
            if board[i][j] == '.':
                return f"({j}, {i})"

        return scan_board(
            board,
            foreach_cell,
            lambda: None,
        )


h = HumanPlayer()
a = AIPlayer()
board = [['x', '.', '.'], ['o', '.', '.'], ['.', '.', '.']]
h.next_move(board)

res = a.next_move(board)
print(res)
