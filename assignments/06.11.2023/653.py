 def dfs(node, seen):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)            
            return dfs(node.left, seen) or dfs(node.right, seen)
        
        return dfs(root, set())