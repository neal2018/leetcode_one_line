class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        return (lambda w_set: (lambda f: max(f(f, w) for w in w_set))(lru_cache(None)(lambda f, w: 1 + max(f(f, w[:j] + w[j + 1:]) if (w[:j] + w[j + 1:]) in w_set else 0 for j in range(len(w))))))(set(words))


# explain
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        return (lambda w_set:  # move words into a set
                (lambda f: max(f(f, w) for w in w_set))(  # dfs on each element
                    lru_cache(None)(  # memo dfs
                        # dfs function
                        # iterate all possible predecessor of w
                        lambda f, w: 1 + max(f(f, w[:j] + w[j + 1:]) if (w[:j] + w[j + 1:]) in w_set
                                             else 0 # if the predecessor not in words
                                             for j in range(len(w)))))
                )(set(words))
