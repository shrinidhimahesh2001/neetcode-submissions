class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        running_sum = 0
        max_sum = float('-inf')
        for i in range(n):
            running_sum+=nums[i]
            max_sum = max(max_sum,running_sum)
            if running_sum<0:
                running_sum = 0
        return max_sum
        