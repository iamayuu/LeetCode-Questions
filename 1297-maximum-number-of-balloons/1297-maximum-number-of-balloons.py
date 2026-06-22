class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {}
        for t in text:
            if t in hmap:
                hmap[t]+=1
            else:
                hmap[t]=1
        
        if 'b' not in hmap or 'a' not in hmap or 'l' not in hmap or 'o' not in hmap or 'n' not in hmap:
            return 0

        count = min(hmap['b'],hmap['a'],hmap['l']//2,hmap['o']//2,hmap['n'])
        return count