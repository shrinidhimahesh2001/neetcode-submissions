class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = 0
        j = len(numbers)-1
        while numbers:
            if k<j and numbers[k]+numbers[j] < target:
                k+=1
            if k<j and numbers[k]+numbers[j] > target:
                j-=1
            if k<j and numbers[k]+numbers[j] == target:
                return [k+1,j+1]
            