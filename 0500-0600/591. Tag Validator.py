from functools import reduce


class Solution:
    def isValid(self, code: str) -> bool:
        return reduce(lambda code, _: re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', '-', code), range(50), re.sub(r'<!\[CDATA\[.*?\]\]>', '-', code)) == "-"


# explain
# regex 50 times
# you can implement a true while loop, but that requires lots more codes.
class Solution:
    def isValid(self, code: str) -> bool:
        return reduce(lambda code, _:
                      re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', '+', code),
                      range(50),
                      re.sub(r'<!\[CDATA\[.*?\]\]>', '-', code)) == "+"
