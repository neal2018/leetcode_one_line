# leetcode one line (in progress...)

Solve all LeetCode problems in one line (Python3)

## Goals

1. The code gets Accpet on LeetCode.
2. Only one line. If the problem requires to implement an interface, then one line for each function required.
3. The codes should use the fastest algorithm when possible.
4. No semicolons, no eval nor similar.
5. The code should be READABLE. (So [onelinerizer](https://github.com/csvoss/onelinerizer) can not help)
6. Add explanation to explain how it works.

## Example

```python
# 1. Two Sum.py
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
```

## Why?

The community LOVES oneliner!

![loves](/figures/loves.png)

(or maybe not...)
