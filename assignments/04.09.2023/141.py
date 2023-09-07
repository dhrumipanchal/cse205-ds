class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return 0

        fast=slow=head
        while(fast.next and fast.next.next):
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return 1

        return 0