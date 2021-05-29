from functools import reduce


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        return (lambda sticks: reduce(lambda cost, _: (lambda stick: (heappush(sticks, stick), cost + stick)[1])(heappop(sticks) + heappop(sticks)), range(len(sticks))))((heapify(sticks), sticks)[1])


# explain
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        return (lambda sticks:
                reduce(lambda cost, _:
                       (lambda stick: # new stick, consisted of two smallest ones
                        (heappush(sticks, stick),
                         cost + stick)[1] # update cost
                        )(heappop(sticks) + heappop(sticks) # pop two smallest ones to form new one
                          ), range(len(sticks)))
                )((heapify(sticks), sticks)[1]) # heapify original sticks
