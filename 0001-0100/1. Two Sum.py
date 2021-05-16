class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(filter(lambda x: x is not None, (lambda nums: (lambda dic: ([dic[n], i] if n in dic else dic.__setitem__(target - n, i) for i, n in enumerate(nums)))({}))(nums)))


# explain
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(  # get the first item
            filter(  # filter not None item
                lambda x: x is not None,
                (lambda nums:  # main function
                 (lambda dic:  # save a dict as a temporary variable
                  # iterate list, if target - n is seen, output the indices
                  # else, put the number into the dict, and output None
                  ([dic[target - n], i] if target - n in dic else dic.__setitem__(n, i) for i, n in enumerate(nums))
                  )({})
                 )(nums)))
