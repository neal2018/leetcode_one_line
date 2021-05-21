class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return (lambda hash_fn: [w for w in words if hash_fn(w) == hash_fn(pattern)])(lambda w: (lambda m: [m.setdefault(c, len(m)) for c in w])({}))


# explain
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return (lambda hash_fn:  # use a hash function to check if the hash val is the same as pattern's
                [w for w in words if hash_fn(w) == hash_fn(pattern)]
                )(
            lambda w: # map the char to the first appear index
            (lambda m: [m.setdefault(c, len(m)) for c in w])({})
        )
