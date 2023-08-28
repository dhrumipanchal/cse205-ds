class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=0
        for i in range (0,len(nums)):
            if len(str(nums[i]))%2==0:
                n=n+1
        return n
