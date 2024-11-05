# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        carry = 0
        while l1 or l2 or carry:
            digit_1 = l1.val if l1 is not None else 0
            digit_2 = l2.val if l2 is not None else 0
            sum = digit_1+digit_2+carry
            carry = 1 if sum>9 else 0
            sum = sum%10
            node = ListNode(sum)
            temp.next = node
            temp = temp.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return res.next