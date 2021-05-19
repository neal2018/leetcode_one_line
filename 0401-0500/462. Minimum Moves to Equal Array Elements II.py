class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return (lambda sorted_nums: sum(abs(x - sorted_nums[len(sorted_nums) // 2]) for x in sorted_nums))(sorted(nums))


# explain
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort to find median, and then move all numbers to median
        return (
            lambda sorted_nums:
                sum(abs(x - sorted_nums[len(sorted_nums) // 2]) for x in sorted_nums)
        )(sorted(nums))
