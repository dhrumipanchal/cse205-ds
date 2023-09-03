class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        maxSum = nums[0]
        curSum = nums[0]  

        for i in range(1, length):  
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)

        return maxSum
