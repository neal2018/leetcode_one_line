class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return self.minKnightMoves(abs(x), abs(y)) if x < 0 or y < 0 else self.minKnightMoves(y, x) if x < y else 3 if x == 1 and y == 0 else 4 if x == y == 2 else x - y - 2 * int((x - 2 * y) // 3) if 2 * y > x else x - y - 2 * int((x - 2 * y) // 4)


# explain
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        return (
            # symmetrics of negative and positive
            self.minKnightMoves(abs(x), abs(y)) if x < 0 or y < 0
            # symmetrics of x and y
            else self.minKnightMoves(y, x) if x < y
            # edge cases
            else 3 if x == 1 and y == 0
            else 4 if x == y == 2
            # math, check https://math.stackexchange.com/questions/1135683/minimum-number-of-steps-for-knight-in-chess
            else x - y - 2 * int((x - 2 * y) // 3) if 2 * y > x
            else x - y - 2 * int((x - 2 * y) // 4))
