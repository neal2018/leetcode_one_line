class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return (lambda dic: max([dic[a] * dic[b] for a, b in itertools.combinations(dic.keys(), 2) if not a & b] or [0]))({sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)})


# expain
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return (lambda dic:  # dic: the character bitmap to the maximum length with this bitmap
                max([  # get the maximum product of lengths
                    dic[a] * dic[b] for a, b in itertools.combinations(dic.keys(), 2)
                    if not a & b  # if a and b do not have common letters
                ] or [0])  # the empty case
                )({sum(1 << (ord(c) - 97) for c in set(w)): len(w)  # bitmap to length
                    for w in sorted(words, key=len)})  # sort by length to ensure we have maximum length in bitmap
