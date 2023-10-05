class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        length=len(nums)
        result=[-1]*length
        for i in range(length*2):
            index=i%length
            while stack and nums[stack[-1]]<nums[index]:
                result[stack.pop()] = nums[index]
            stack.append(index)
        return result