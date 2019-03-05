class ParseMoveError(Exception):
    def __init__(self):
        super().__init__("Sorry I don't understand")


class InvalidMoveError(Exception):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col


def try_to_read_move_from_player():
    raise InvalidMoveError(10, 20)


try:
    try_to_read_move_from_player()
except InvalidMoveError as err:
    print('1 ... you cant do that')
    print(err.row, err.col)

except ParseMoveError as err:
    print(err)
