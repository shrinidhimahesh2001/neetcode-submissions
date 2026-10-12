class Solution:
    def maxArea(self, heights: List[int]) -> int:
        distance=0
        n = len(heights)
        i=0
        j=n-1
        max_vol=0
        while i<j:
            distance = j-i
            volume = min(heights[i],heights[j])*distance
            max_vol = max(max_vol, volume)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_vol