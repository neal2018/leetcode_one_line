class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return (lambda hh, ww: (max(b - a for a, b in zip(hh, hh[1:])) * max(b - a for a, b in zip(ww, ww[1:]))) % (10**9 + 7))([0] + sorted(horizontalCuts) + [h], [0] + sorted(verticalCuts) + [w])


# explain
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return (lambda hh, ww: # find the maximum gap
                (max(b - a for a, b in zip(hh, hh[1:])) * max(b - a for a, b in zip(ww, ww[1:]))) % (10**9 + 7)
                )([0] + sorted(horizontalCuts) + [h], [0] + sorted(verticalCuts) + [w])
