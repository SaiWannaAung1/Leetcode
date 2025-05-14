# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def to_number(node):
            digits = []
            while node:
                digits.append(str(node.val))
                node = node.next
            return int(''.join(digits[::-1]))

        total = to_number(l1) + to_number(l2)
        dummy = ListNode()
        current = dummy
        for d in str(total)[::-1]:
            current.next = ListNode(int(d))
            current = current.next
        return dummy.next


        
        