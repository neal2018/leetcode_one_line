class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        return (lambda s: ([(lambda p_split:[(lambda f_split:s[f_split[1]].append(f"{p_split[0]}/{f_split[0]}"))(f[:-1].split("(")) for f in p_split[1:]])(p.split(" ")) for p in paths], [v for v in s.values() if len(v) > 1])[1])(defaultdict(list))


# explain
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        return (lambda s:  # s is a defaultdict
                (  # returns a tuple, first one is for preprocessing, and second one is the answer
                    [(lambda p_split:  # p_split is p in path split by " "
                      [(lambda f_split:  # f_split is file in p_split split by "("
                        s[f_split[1]].append(f"{p_split[0]}/{f_split[0]}")  # save the path and content into s
                        )(f[:-1].split("(")) for f in p_split[1:]]  # iterate file in p
                      )(p.split(" ")) for p in paths],  # iterate p in path
                    [v for v in s.values() if len(v) > 1]  # filter repeating ones
                )[1]  # get the second one in the tuple to return
                )(defaultdict(list))
