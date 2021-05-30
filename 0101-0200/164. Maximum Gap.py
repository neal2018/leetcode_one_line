class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return (lambda mini, maxi: 0 if len(nums) < 0 or mini == maxi else (lambda buckets: max(b[0] - a[1] for a, b in zip(buckets, buckets[1:])))(list(filter(lambda bucket: bucket[0] is not None, (lambda size: (lambda buckets: ([(lambda index:buckets.__setitem__(index, [num, num] if buckets[index][0] is None else [min(buckets[index][0], num), max(buckets[index][1], num)]))((num - mini) // size) for num in nums], buckets)[-1])([[None, None] for _ in range((maxi - mini) // size + 1)]))((maxi - mini) // (len(nums) - 1) or 1)))))(min(nums), max(nums))


# explain
# bucket sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return (lambda mini, maxi: 0 if len(nums) < 0 or mini == maxi else  # corner case
                (lambda buckets:  # receive a bucket and return the max diff between buckets
                 max(b[0] - a[1] for a, b in zip(buckets, buckets[1:]))
                 )(  # now we construct the bucket
                     list(filter(lambda bucket:
                                 bucket[0] is not None,  # filter out empty buckets
                                 (lambda size:  # calculate the size of buckets
                                  (lambda buckets:  # iterate nums to fill buckets
                                   ([(lambda index:  # for each num, calculate the buckets[index] it belongs to
                                     buckets.__setitem__(index,  # update that bucket
                                                         [num, num] if buckets[index][0] is None
                                                         else [min(buckets[index][0], num), max(buckets[index][1], num)]
                                                         )
                                      )((num - mini) // size)  # calculate the index
                                     for num in nums
                                     ], buckets)[-1]  # return the filled buckets
                                   )([[None, None] for _ in range((maxi - mini) // size + 1)])  # initial empty buckets
                                  )((maxi - mini) // (len(nums) - 1) or 1)  # calculate the size of buckets
                                 ))
        )
        )(min(nums), max(nums))
