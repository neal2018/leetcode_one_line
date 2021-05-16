class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return reduce(lambda acc, x: (j := max(acc[0], acc[1].get(x[1], -1)), (acc[1].__setitem__(x[1], x[0]) or acc[1]), max(acc[2], x[0] - j)), enumerate(s), (-1, {}, 0))[2]


# explain
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return reduce(
            # x is gain from iterating enumerate(s), so x = (i, v)
            # we maintain acc = (j, dict, ans)
            # where j is the smallest index s.t. s[j+1:i+1] contains no repeating char
            # dict[c] is the nearest index contain char c by far
            # ans is the maximum length we want
            lambda acc, x: (j := max(acc[0], acc[1].get(x[1], -1)),
                            # update dict and output dict
                            (acc[1].__setitem__(x[1], x[0]) or acc[1]),
                            max(acc[2], x[0] - j)),
            enumerate(s), # iterate s
            (-1, {}, 0) # initial value
            )[2] # take the last one, i.e., ans
