class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        return (lambda node: (lambda f, node: f(f, node))(lambda f, node: (lambda left, right: (min(left[1] + right[1], 1 + left[0] + right[0]), 1 + min(left[0] + right[0], left[2] + right[1], left[1] + right[2]), left[0] + right[0]))(f(f, node.left), f(f, node.right)) if node else (0, 0, inf), node))(root)[1]


# explain
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        return (lambda node:
                (lambda f, node:  # Y combination to implement recursion
                 f(f, node))(
                    lambda f, node:  # main recursion function
                    # returns the camera required for (node is seen, node is not seen, node is already camera)
                    (lambda left, right:  # the recursion result of left and right
                     (min(1 + left[0] + right[0], left[1] + right[1]),
                      1 + min(left[0] + right[0], left[2] + right[1], left[1] + right[2]),
                      left[0] + right[0])
                     )(f(f, node.left), f(f, node.right)) # the recursion result of left and right
                    if node else (0, 0, inf),  # base case
                    node)  # Y combination ends
                )(root)[1]  # the root is not seen, so return the second item
