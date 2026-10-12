class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left=0
        result=0
        for i in range(0,len(s)):
            if s[i] in seen:
                left=max(seen[s[i]]+1,left)
            seen[s[i]]=i
            result=max(result,i-left+1)
        return result