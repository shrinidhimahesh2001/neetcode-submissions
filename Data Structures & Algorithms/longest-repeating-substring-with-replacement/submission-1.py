from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        counts = [0]*26
        for r in range(len(s)):
            counts[ord(s[r])-65]+=1
            while (r-left+1) - max(counts) > k:
                counts[ord(s[left])-65]-=1
                left +=1
            longest = max(longest,(r-left+1))
        return longest