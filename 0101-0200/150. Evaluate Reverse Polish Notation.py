class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return (lambda stack, op: ([stack.append(int(op[t](stack.pop(-2), stack.pop(-1))) if t in op else int(t)) for t in tokens], stack[0])[1])([], {'+': add, '-': sub, '*': mul, '/': truediv})


# expain
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return (lambda stack, op:  # use a stack
                ([stack.append(int(op[t](stack.pop(-2), stack.pop(-1))) if t in op  # when meeting ops, pop the last two and calculate result
                               else int(t))  # else, put it into stack
                    for t in tokens],
                    stack[0])[1]  # return the remaining item in stack
                )([], {'+': add, '-': sub, '*': mul, '/': truediv})
