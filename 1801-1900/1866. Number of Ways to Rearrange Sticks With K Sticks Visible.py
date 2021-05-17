class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        return (lambda MOD: (lambda f, n, k: f(f, n, k))(lru_cache(None)(lambda f, n, k: 1 if n == k else 0 if k == 0 else (f(f, n - 1, k - 1) + f(f, n - 1, k) * (n - 1)) % MOD), n, k))(10**9 + 7)


# explain
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        return (lambda MOD:  # variable MOD to save 10**9 + 7
                (lambda f, n, k: f(f, n, k))(  # Y combination to implement recursion
                    # lru_cache to implement memoization
                    lru_cache(None)(
                        lambda f, n, k:  # real recursion function
                        (   # edge cases
                            1 if n == k
                            else 0 if k == 0
                            # consider the shortest sticks. there is n places we can put it into
                            # if we put it into the leftest place, it must be seen. hence we decrement k
                            # if we put it into other n-1 places, it must not be seen. hence k remains
                            else (f(f, n - 1, k - 1) + f(f, n - 1, k) * (n - 1)) % MOD
                        )),
                    n, k)
                )(10**9 + 7)
