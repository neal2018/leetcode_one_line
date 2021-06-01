from functools import reduce


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return min(reduce(lambda colors, cost: [cost[i] + min(colors[j] for j in range(len(cost)) if j != i) for i in range(len(cost))], costs))


# expain
# dp
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        return min(
            reduce(
                lambda colors, cost:  # colors[x] the minimal cost so far with the last one being color x
                [cost[i] + min(colors[j] for j in range(len(cost)) if j != i)
                 for i in range(len(cost))], costs))
