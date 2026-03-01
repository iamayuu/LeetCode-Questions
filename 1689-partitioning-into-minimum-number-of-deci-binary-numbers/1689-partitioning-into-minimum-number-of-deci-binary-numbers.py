class Solution:
    def minPartitions(self, n: str) -> int:
        max_s = 0
        for s in n:
            max_s = max(max_s,int(s))
        return max_s