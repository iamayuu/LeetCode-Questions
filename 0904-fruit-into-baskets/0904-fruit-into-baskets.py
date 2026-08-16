class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        maxFruits = 0
        bucketsNeeded = 0
        hmap = dict()
        j = 0
        for i in range(n):
            fruit = fruits[i]
            if fruit not in hmap:
                hmap[fruit]=1
            else:
                hmap[fruit]+=1
            bucketsNeeded = len(hmap)
            while bucketsNeeded>2:
                hmap[fruits[j]]-=1
                if hmap[fruits[j]]==0:
                    del hmap[fruits[j]]
                bucketsNeeded = len(hmap)
                j+=1

            if bucketsNeeded<=2:
                maxFruits = max(maxFruits, (i-j+1))
                
        return maxFruits