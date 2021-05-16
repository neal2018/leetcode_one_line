# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return (lambda val: ListNode(val % 10, self.addTwoNumbers(ListNode(l1.next.val + val // 10, l1.next.next) if l1.next else ListNode(val // 10), l2.next if l2.next else ListNode(0))) if any((l1.next, l2.next, val // 10)) else ListNode(val % 10))(l1.val + l2.val)


# explain
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return (lambda digit, carry:  # the digit and tenth of l1.val + l2.val
                ListNode(digit,  # the return target
                         self.addTwoNumbers(
                             # next l1, but put the carry into l1
                             ListNode(l1.next.val + carry, l1.next.next) if l1.next else ListNode(carry),
                             # next l2
                             l2.next if l2.next else ListNode(0)))
                if any((l1.next, l2.next, carry)) else ListNode(digit)  # do not need to recurse
                )((l1.val + l2.val) % 10, (l1.val + l2.val) // 10)  # put value into digit and carry
