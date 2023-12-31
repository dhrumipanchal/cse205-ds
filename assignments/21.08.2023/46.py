from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums,[],result)
        return result
    
    def dfs(self,nums,path,result):
        if not nums:
            result.append( path[:] )  
            return
        for i in range( len(nums) ):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)