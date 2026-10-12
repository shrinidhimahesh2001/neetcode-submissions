class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen=[]
        nums=sorted(nums)
        n=len(nums)
        for i in range(0,n-2):
            left=i+1
            right=n-1
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
#                continue
                else :
                    seen.append([-target, nums[left],nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right-=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
#                continue
        return seen