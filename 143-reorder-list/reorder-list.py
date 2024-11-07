# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        prev = None
        slow.next = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid 
            mid = temp
        first_half, second_half = head, prev
        while second_half:
            temp_1, temp_2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp_1
            first_half, second_half = temp_1, temp_2
        return head

