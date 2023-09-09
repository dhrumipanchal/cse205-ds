# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current=slow=fast=ListNode()
        current.next=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next

        dummy=None
        h1=slow.next
        
        while h1:
            new=h1.next
            h1.next = dummy
            dummy=h1
            h1=new

        while dummy:
            if head.val==dummy.val:
                head=head.next
                dummy=dummy.next
            else:
                return False

        if not dummy:
            return True