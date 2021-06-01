class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return (lambda n, m: (lambda seen: (lambda dfs: max(dfs(dfs, i, j) for i in range(n) for j in range(m)))(lambda f, i, j: 0 if not (0 <= i < n and 0 <= j < m) or grid[i][j] != 1 or (i, j) in seen else (seen.add((i, j)), 1 + sum(f(f, ii, jj) for ii, jj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]))[-1]))(set()))(len(grid), len(grid[0]))


# explain
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return (lambda n, m:  # n, m = len(grid), len(grid[0])
                (lambda seen:  # mark seen nodes
                 (lambda dfs:  # run dfs on all nodes
                  max(dfs(dfs, i, j) for i in range(n) for j in range(m))
                  )(lambda f, i, j:  # implement dfs
                    0 if not (0 <= i < n and 0 <= j < m) or grid[i][j] != 1 or (i, j) in seen  # invalid cases
                    else (
                        seen.add((i, j)),  # mark seen
                        # recursive dfs
                        1 + sum(f(f, ii, jj) for ii, jj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]])
                    )[-1])
                 )(set())  # input seen
                )(len(grid), len(grid[0]))  # input n, m
