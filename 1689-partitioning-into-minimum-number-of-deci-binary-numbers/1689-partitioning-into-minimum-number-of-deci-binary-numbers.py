class Solution:
    def minPartitions(self, n: str) -> int:
        max_s = '0'
        for s in n:
            max_s = max(max_s,s)
            if max_s=='9':
                return int(max_s)
        return int(max_s)