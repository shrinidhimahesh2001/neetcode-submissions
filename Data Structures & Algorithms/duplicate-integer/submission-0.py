class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        j=0
        flag = 0
        for i in range (0,len(nums)-1):
            val=nums[j]
            if val==nums[i+1]:
                flag+=1
            j+=1     
        if flag==0:
            return False
        else:
            return True
