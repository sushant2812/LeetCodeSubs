# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        while temp_head.next!=None:
            next_node = temp_head.next
            new_value = math.gcd(next_node.val,temp_head.val)
            new_Node = ListNode()
            new_Node.val = new_value
            new_Node.next = next_node
            temp_head.next = new_Node
            temp_head = next_node
        return head