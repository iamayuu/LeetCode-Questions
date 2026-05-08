class Solution:
    def hammingWeight(self, n: int) -> int:
        setBits = 0
        while n>0:
            if n&1!=0:
                setBits+=1
            n=n>>1
        return setBits