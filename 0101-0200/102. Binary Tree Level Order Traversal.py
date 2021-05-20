# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return [] if not root else [[root.val]] + [a + b for a, b in zip_longest(self.levelOrder(root.left), self.levelOrder(root.right), fillvalue=[])]


# explain
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return [] if not root else [  # base cases
            [root.val]] + [ # dfs
                a + b for a, b in zip_longest(self.levelOrder(root.left), self.levelOrder(root.right), fillvalue=[])
        ]
