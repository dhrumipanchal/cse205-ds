# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        cols=defaultdict(list)

        def dfs(node,row,col):
            if not node:
                return

            heappush(cols[col],(row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)

        dfs(root,0,0)
        result=[]
        for col in sorted(cols):
            result.append([val for row, val in sorted(cols[col])])

        return result