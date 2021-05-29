class Solution:
    def totalNQueens(self, n: int) -> int:
        return (lambda backtracking: backtracking(backtracking, 0, 0, 0, 0))(lambda f, row, cols, ds, anti_ds: 1 if row == n else sum((lambda x: f(f, row + 1, cols | x, (ds | x) << 1, (anti_ds | x) >> 1) if not (cols & x or ds & x or anti_ds & x) else 0)(1 << i) for i in range(n)))


# explain
class Solution:
    def totalNQueens(self, n: int) -> int:
        return (lambda backtracking:
                backtracking(backtracking, 0, 0, 0, 0)
                )(lambda f, row, cols, ds, anti_ds: # backtracking function
                  1 if row == n # base case
                  else sum( # try all possibilities
                      (lambda x: f(f, row + 1, cols | x, (ds | x) << 1, (anti_ds | x) >> 1) if not (cols & x or ds & x or anti_ds & x)
                       else 0 # if no available place
                       )(1 << i) for i in range(n)))
