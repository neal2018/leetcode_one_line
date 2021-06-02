class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return False if len(s3) != len(s1) + len(s2) else (lambda dfs: dfs(dfs, len(s1), len(s2)))(lru_cache(None)(lambda f, i, j: True if i == 0 and j == 0 else (i > 0 and s1[i - 1] == s3[i + j - 1] and f(f, i - 1, j)) or (j > 0 and s2[j - 1] == s3[i + j - 1] and f(f, i, j - 1))))


# explain
# top-down dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return False if len(s3) != len(s1) + len(s2) else (  # length check
            lambda dfs: dfs(dfs, len(s1), len(s2))  # dp call
        )(lru_cache(None)(  # memo
            lambda f, i, j: True if i == 0 and j == 0 else (  # base case
                i > 0 and s1[i - 1] == s3[i + j - 1] and f(f, i - 1, j))  # recursive call
            or (j > 0 and s2[j - 1] == s3[i + j - 1] and f(f, i, j - 1))))
