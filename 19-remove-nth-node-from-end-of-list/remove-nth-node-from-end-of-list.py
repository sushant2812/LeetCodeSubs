# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        slow = res 
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            slow = slow.next
        slow.next=slow.next.next
        return res.next