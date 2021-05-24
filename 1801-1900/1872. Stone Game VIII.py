class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        return (lambda presum: (lambda dp: dp(dp, 0))(lru_cache(None)(lambda dp, k: presum[-1] if len(stones) == k + 2 else max(presum[k + 1] - dp(dp, k + 1), dp(dp, k + 1)))))(list(accumulate(stones)))


# explain
# it is a top-down dp
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        return (lambda presum:  # presum[i] = sum(stones[0]...stones[i]), inclusive
                (lambda dp:  # dp(k) = the maximum diff given that up to k-th stones are merged together
                 dp(dp, 0)  # start with no stone merged together
                 )(  # implement dp function
                     lru_cache(None)(  # add memo
                         lambda dp, k:
                         presum[-1] if len(stones) == k + 2  # base case
                         else max(presum[k + 1] - dp(dp, k + 1),  # chose picking only first and second
                                  # other options, must pick first and second,
                                  # treat as first and second merged together
                                  dp(dp, k + 1)))
                )
                )(list(accumulate(stones)))  # calculate prefix sum
