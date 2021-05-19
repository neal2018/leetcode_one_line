class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return (lambda medians: (lambda pivot: (lambda l, e, h: self.findKthLargest(h, k) if k <= len(h) else self.findKthLargest(l, k - len(h) - len(e)) if k > len(h) + len(e) else pivot)([j for j in nums if j < pivot], [j for j in nums if j == pivot], [j for j in nums if j > pivot]))(sorted(medians)[len(medians) // 2] if len(medians) <= 5 else self.findKthLargest(medians, len(medians) // 2 + 1)))((lambda sub_lists: [sorted(s)[len(s) // 2] for s in sub_lists])([nums[i:i + 5] for i in range(0, len(nums), 5)]))


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # median of medians + quick select
        return (lambda medians:  # medians: a list of median of sublists
                (lambda pivot:  # pivot, equaling to the median in medians
                 (lambda l, e, h:  # low, equal, high, partited nums by pivot
                  self.findKthLargest(h, k) if k <= len(h)  # recursion call
                  else self.findKthLargest(l, k - len(h) - len(e)) if k > len(h) + len(e)
                  else pivot
                  )(  # partited list by pivot
                      [j for j in nums if j < pivot],   # low
                      [j for j in nums if j == pivot],  # equal
                      [j for j in nums if j > pivot]    # high
                 )
                 )(  # find the median in medians
                     sorted(medians)[len(medians) // 2] if len(medians) <= 5  # if median is short, just sort
                     else self.findKthLargest(medians, len(medians) // 2 + 1)  # else, recursion call
                )
                )(  # find out medians of sublists
                    (lambda sub_lists:
                     # sort and get the median, since each sublist is short
                     [sorted(s)[len(s) // 2] for s in sub_lists]
                     )(  # split nums into sublists whose maximum length is 5
                         [nums[i:i + 5] for i in range(0, len(nums), 5)]
                    )
        )
