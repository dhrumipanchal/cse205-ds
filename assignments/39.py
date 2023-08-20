from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def com_sum(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            com_sum(i, current, total + candidates[i])
            current.pop()
            com_sum(i + 1, current, total)
        
        com_sum(0, [], 0)
        return result
