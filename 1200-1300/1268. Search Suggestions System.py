class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        return (lambda ans: ((lambda products: reduce(lambda curr, c: ((lambda i: ans.append([p for p in products[i:i + 3] if p.startswith(curr + c)]))(bisect_left(products, curr + c)), curr + c)[-1], searchWord, ""))(sorted(products)), ans)[-1])([])


# explain
# sort + binary search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        return (lambda ans:
                ((lambda products:  # get a sort products
                  reduce(lambda curr, c:  # curr search string, current character
                         ((lambda i:
                           ans.append([p for p in products[i:i + 3] if p.startswith(curr + c)])
                           )(bisect_left(products, curr + c))  # binary search
                          , curr + c)[-1], searchWord, "")
                  )(sorted(products)),  # input a sorted products
                 ans)[-1])([])  # return ans
