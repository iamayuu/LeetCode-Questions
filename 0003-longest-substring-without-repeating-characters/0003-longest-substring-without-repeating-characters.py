class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hmap = dict()
        maxLen = 0
        j=0
        for i in range(n):
            if s[i] in hmap:
               hmap[s[i]]+=1
            else:
               hmap[s[i]]=1
            
            while hmap[s[i]]>1:
                hmap[s[j]]-=1
                j+=1
            
            maxLen = max(maxLen,(i-j+1))
        
        return maxLen