class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if len(nums)==1:
                return nums[0]
            elif nums[i]< nums[i-1]:
                return nums[i]
                break
        