class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return (lambda ans: ((lambda f, rows, cols, diagonals, anti_diagonals, state: f(f, rows, cols, diagonals, anti_diagonals, state))(lambda f, rows, cols, diagonals, anti_diagonals, state: ans.append(["." * v + "Q" + "." * (n - v - 1) for v in state]) if rows == n else [[state.append(i), f(f, rows + 1, cols | (1 << i), (diagonals | (1 << i)) >> 1, (anti_diagonals | (1 << i)) << 1, state), state.pop()] for i in range(n) if not (cols & (1 << i) or diagonals & (1 << i) or anti_diagonals & (1 << i))], 0, 0, 0, 0, []), ans)[1])([])


# explain
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return (lambda ans:
                ((lambda f, rows, cols, diagonals, anti_diagonals, state:  # Y combination
                  f(f, rows, cols, diagonals, anti_diagonals, state))(
                    lambda f, rows, cols, diagonals, anti_diagonals, state:  # real backtracking function
                    ans.append(["." * v + "Q" + "." * (n - v - 1) for v in state]) if rows == n  # reach destination
                    else [
                        [state.append(i),  # add current state
                         f(f,  # mark seen and recurse
                            rows + 1,
                            cols | (1 << i),
                            (diagonals | (1 << i)) >> 1,
                            (anti_diagonals | (1 << i)) << 1,
                            state),
                         state.pop()]  # pop out current state
                        for i in range(n)
                        # can not collide with previous ones
                        if not (cols & (1 << i) or diagonals & (1 << i) or anti_diagonals & (1 << i))
                    ], 0, 0, 0, 0, []), ans)[1] # put ans in the second place to return
                )([])
