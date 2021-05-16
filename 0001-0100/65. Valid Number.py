class Solution:
    def isNumber(self, s: str) -> bool:
        return re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$").match(s)


# explain
# simple regex
