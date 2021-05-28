class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        return (lambda num2sum: reduce(lambda x, num: ((x[0] + num, max(x[1], num2sum[num]), max(x[2], x[0] + num - max(x[1], num2sum[num]))), num2sum.__setitem__(num, x[0] + num))[0], nums, (0, 0, 0)))(defaultdict(int))[-1]


# explain
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        return (lambda num2sum: # dict storign nearest num to its prefix-sum
                reduce( # maintain (current prefix sum, nearest non-repeating prefix sum, max result)
                    lambda x, num:
                    ((
                        x[0] + num, # current prefix sum update to previous add current number
                        max(x[1], num2sum[num]), # update nearest non-repeating prefix sum
                        max(x[2], x[0] + num - max(x[1], num2sum[num])) # max result
                    ),
                        num2sum.__setitem__(num, x[0] + num))[0], # update dict
                    nums, # iterate nums
                    (0, 0, 0) # initial values
                ))(defaultdict(int) # initial num2sum
                   )[-1] # pick the last one which is max result to return
