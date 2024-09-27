# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for a in lists:
            while a:
                values.append(a.val)
                a=a.next
        values = heapsort(values)
        head = ListNode()
        temp = head
        for num in values:
            temp.next = ListNode(num)
            temp = temp.next
        return head.next