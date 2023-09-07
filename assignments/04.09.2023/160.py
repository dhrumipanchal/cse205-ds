# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA==None or headB==None:
            return None
        
        dummy1=headA
        dummy2=headB

        while dummy1!=dummy2:
            dummy1 = dummy1.next if dummy1 != None else headB
            dummy2 = dummy2.next if dummy2 != None else headA

        return dummy1

