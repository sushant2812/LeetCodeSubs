# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
def heapsort(lst):
    h = []
    for i in range(len(lst)):
        heappush(h,lst[i])
    return [heappop(h) for i in range(len(lst))]
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for lst in lists:
            while lst:
                values.append(lst.val)
                lst=lst.next
        
        new_values = heapsort(values)
        head=ListNode()
        temp=head 
        for num in new_values:
            temp.next = ListNode(num)
            temp = temp.next
        return head.next