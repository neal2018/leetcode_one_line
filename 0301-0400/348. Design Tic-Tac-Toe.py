class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.count, self.n = {}, n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        return (lambda cnt_list: player if any(True for i in cnt_list if i[1] == True) else 0)([(self.count.__setitem__((i, x, player), self.count.get((i, x, player), 0) + 1), self.count[(i, x, player)] == self.n, player) for i, x in enumerate((row, col, row + col, row - col))])


# explain
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.count, self.n = {}, n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        return (
            lambda cnt_list:  # the count marks of current player in row, col, diagonal, and anti diagonal
            player if any(True for i in cnt_list if i[1] == True) else 0  # if there is any cnt==n, current player wins
        )(  # update the current move before previous steps
            [(self.count.__setitem__((i, x, player), self.count.get((i, x, player), 0) + 1),  # cnt+=1
              self.count[(i, x, player)] == self.n  # cnt==n or not
              ) for i, x in enumerate((row, col, row + col, row - col))]
        )
