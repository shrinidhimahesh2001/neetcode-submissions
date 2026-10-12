import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        #result =[]
        for val in nums:
            if val in freq:
                freq[val]+=1
            else:
                freq[val]=1
        return heapq.nlargest(k, freq.keys(), key=freq.get)
        