class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return (lambda f, n: f(f, n))(lru_cache(None)(lambda f, n: any((not f(f, n - i * i)) for i in range(int(sqrt(n)), 0, -1)) if n > 0 else False), n)


# explain
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return (lambda f, n: f(f, n))(  # Y combination to implement recursion
            lru_cache(None)(  # cache
                lambda f, n:  # real recursion function
                # check all possible move and whether exists a situation where opponent must fail
                any((not f(f, n - i * i)) for i in range(int(sqrt(n)), 0, -1)) if n > 0 else False
            ), n)
