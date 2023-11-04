# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1

        def isMirror(left,right):
            if not left and not right:
                return 1
            if not left or not right:
                return 0
            return left.val==right.val and isMirror(left.left,right.right) and isMirror(left.right,right.left)

        return isMirror(root.left,root.right)