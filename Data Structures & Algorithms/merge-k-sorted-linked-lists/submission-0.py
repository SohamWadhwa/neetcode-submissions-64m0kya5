# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        minHeap = []

        for i, ls in enumerate(lists):
            if ls:
                heapq.heappush(minHeap, (ls.val , i, ls))
        
        dummy = ListNode(-1)
        ptr = dummy

        while minHeap:
            val, idx, ls = heapq.heappop(minHeap)

            ptr.next = ls
            ptr = ptr.next

            if ls.next:
                heapq.heappush(minHeap, (ls.next.val, idx, ls.next))
        
        return dummy.next