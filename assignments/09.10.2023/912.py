class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(left,right):
            merged=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            while i<len(left):
                merged.append(left[i])
                i+=1
            while j<len(right):
                merged.append(right[j])
                j+=1
            return merged

        def merge(nums):
            if len(nums)<2:
                return nums
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]
            
            left=merge(left)
            right=merge(right)
            return mergesort(left,right)
        
        return merge(nums)