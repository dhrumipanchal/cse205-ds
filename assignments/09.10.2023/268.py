class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=[]
        l=len(nums)
        for n in range(0, l+1):
            if n not in nums:
                return n
            
                 