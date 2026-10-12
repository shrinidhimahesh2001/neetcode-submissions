class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
 #       for i in range (0, n-1):
        left = 0 
        right = n-1
        #mid = (left+right)//2
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left=mid+1
        return nums[left]
        