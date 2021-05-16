class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        return (lambda split: [f"({x}, {y})" for i in range(2, len(s) - 1) for y in split(s[i:-1]) for x in split(s[1:i])])(lambda s: ([f"{s[:i]}.{s[i:]}" for i in range(1, len(s)) if s[-1] != "0"] + [s]) if s[0] != "0" else ([f"{s[0]}.{s[1:]}"] if s[-1] != "0" else ([s] if s == "0" else [])))


# explain
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        return (lambda split:
                # iterate all possible cut of s; split the cut put into all possible decimals
                [f"({x}, {y})" for i in range(2, len(s) - 1) for y in split(s[i:-1]) for x in split(s[1:i])])(
            # split function
            lambda s: ([f"{s[:i]}.{s[i:]}" for i in range(1, len(s)) if s[-1] != "0"] + [s])  # if s[0] is 0
            # if s[0] is not 0
            if s[0] != "0" else ([f"{s[0]}.{s[1:]}"] if s[-1] != "0" else ([s] if s == "0" else [])))
