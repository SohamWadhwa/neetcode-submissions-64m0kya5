class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            kth = self.getKthNode(prev_group_end, k)
            if not kth:
                break
            
            group_start = prev_group_end.next
            next_group = kth.next
      
            self.reverseList(group_start, kth)
            
            prev_group_end.next = kth
            
            
            prev_group_end = group_start
        
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr  

    def reverseList(self, start, end):
        prev = end.next
        curr = start
        
        while prev != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt