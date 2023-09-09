# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head
        pre = dummy
        nex = dummy
        cur = dummy

        count = 0
        while cur.next:
            count += 1
            cur = cur.next

        while count >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k-1):
                if not nex:
                    break
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            count -= k
            pre = cur

        return dummy.next
