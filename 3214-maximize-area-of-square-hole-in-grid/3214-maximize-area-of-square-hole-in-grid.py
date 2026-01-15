class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxSubseqH, maxSubseqV = 1, 1
        crr_maxSubseq = 1
        for i in range(len(hBars)-1):
            if hBars[i+1] == hBars[i]+1:
                crr_maxSubseq+=1
            else:
                crr_maxSubseq=1
            maxSubseqH = max(maxSubseqH, crr_maxSubseq)
        crr_maxSubseq = 1
        for i in range(len(vBars)-1):
            if vBars[i+1] == vBars[i]+1:
                crr_maxSubseq+=1
            else:
                crr_maxSubseq=1
            maxSubseqV = max(maxSubseqV, crr_maxSubseq)
        return (min(maxSubseqH, maxSubseqV)+1)**2