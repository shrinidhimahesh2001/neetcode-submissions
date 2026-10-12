#from collections import deque
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = dict()
        result = []
        for i,val in enumerate(nums):
            complement = target-val
            if complement in pairs:
                return [pairs[complement],i]
            else:
                pairs[val] = i


        