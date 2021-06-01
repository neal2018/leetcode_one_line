class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return min(reduce(lambda colors, cost: (cost[0] + min(colors[1], colors[2]), cost[1] + min(colors[2], colors[0]), cost[2] + min(colors[0], colors[1])), costs))


# explain
# dp
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        return min(
            reduce(lambda colors, cost:  # colors[x] the minimal cost so far with the last one being color x
                   (
                       cost[0] + min(colors[1], colors[2]),
                       cost[1] + min(colors[2], colors[0]),
                       cost[2] + min(colors[0], colors[1])
                   ),
                   costs))
