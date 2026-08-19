from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        n = len(s)
        l = 0
        res = 0
        for r in range(n):
            hmap[s[r]]+=1
            maxFreq = max(hmap.values())

            while ((r-l+1)-maxFreq) > k:
                hmap[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
        
        return res