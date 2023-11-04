# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        rv=preorder[0]
        root=TreeNode(rv)
        ri=inorder.index(rv)
        root.left=self.buildTree(preorder[1:ri+1], inorder[:ri])
        root.right=self.buildTree(preorder[ri+1:], inorder[ri+1:])
        return root