# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=ListNode()
        curr.next=head
        n1=n2=curr
        while n2.next and n2.next.next:
            n2=n2.next.next
            n1=n1.next
        return n1.next
        