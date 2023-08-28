class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result=0
        counter=0
        for n in nums:
            if n==1:
                counter=(counter+1)
            else:
                counter=0
            result=max(result,counter)
        return result