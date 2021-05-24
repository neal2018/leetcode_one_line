# base on https://leetcode.com/problems/find-the-shortest-superstring/discuss/1225543/Python-dp-on-subsets-solution-3-solutions-%2B-oneliner-explained
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        return (lambda n: (lambda get_dis: (lambda dfs: min((words[i] + dfs(dfs, i, 1 << i) for i in range(n)), key=len))(lru_cache(None)(lambda dfs, node, mask: "" if mask == (1 << n) - 1 else min((words[i][-get_dis(words[node], words[i]):] + dfs(dfs, i, mask | (1 << i)) for i in range(n) if not mask & (1 << i)), key=len))))(lru_cache(None)(lambda w1, w2: min([len(w2) - len(w1[i:]) for i in range(len(w1)) if w1[i:] == w2[:len(w1[i:])]] + [len(w2)]))))(len(words))


# explain
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        return (lambda n:  # len(words)
                (lambda get_dis:  # get_dis(i,j) calculates the len of string need to add if append words[j] to words[i]
                 (lambda dfs:  # backtracking function
                  min((words[i] + dfs(dfs, i, 1 << i) for i in range(n)), key=len)
                  )(  # implement backtracking function
                      lru_cache(None)(  # add memo
                          lambda dfs, node, mask:
                          "" if mask == (1 << n) - 1  # if add all words, not need to continue
                          else min((words[i][-get_dis(words[node], words[i]):]  # else, if haven't seen i,  get the un-overlap part
                                    + dfs(dfs, i, mask | (1 << i))  # recursion add the rest words
                                    for i in range(n)  # try all possibility for i
                                    if not mask & (1 << i)), key=len))  # filter i that haven't been seen
                 )
                 )(  # implement get_dis function
                     lru_cache(None)(  # add memo
                         lambda w1, w2:
                         # find the longest suffix of w1 which is the prefix of w2, return the len of remaining part of w2
                         min([len(w2) - len(w1[i:])
                              for i in range(len(w1)) if w1[i:] == w2[:len(w1[i:])]]
                             + [len(w2)]))  # the empty case
                )
                )(len(words))
