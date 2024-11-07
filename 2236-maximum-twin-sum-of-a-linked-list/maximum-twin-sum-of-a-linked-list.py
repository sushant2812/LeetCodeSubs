# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        max_sum =0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        start=head
        while prev:
            max_sum=max(max_sum,prev.val+start.val)
            start=start.next
            prev=prev.next
        return max_sum