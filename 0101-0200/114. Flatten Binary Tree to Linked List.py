class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        (setattr(self, "next", None), (lambda f, node: f(f, node))(lambda f, node: node and (f(f, node.right), f(f, node.left), setattr(node, "left", None), setattr(node, "right", self.next), setattr(self, "next", node)), root))

# explain


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        (setattr(self, "next", None),  # store a next variable pointing to the next node we want
         (lambda f, node:  # Y combination to implement recursion
          f(f, node))(
            lambda f, node:  # real recursion function
            node and  # if node is None, skip following steps
            (f(f, node.right), f(f, node.left),  # recurse left and right
             # update attribution of node to meet the problem requirement
             setattr(node, "left", None), setattr(node, "right", self.next), setattr(self, "next", node)
             ),
            root)  # Y combination ends
         )
