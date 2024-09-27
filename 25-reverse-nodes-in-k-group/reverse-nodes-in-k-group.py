# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start, end):
            prev = end
            curr = start
            while curr != end:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count == k: 
            reversed_head = reverseLinkedList(head, curr)
            head.next = self.reverseKGroup(curr, k)
            return reversed_head
        
        return head
