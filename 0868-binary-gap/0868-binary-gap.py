class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        last_found_idx = 0
        ans = 0
        for i,bit in enumerate(binary):
            if bit=='1':
                ans = max(ans, i-last_found_idx)
                last_found_idx=i
        return ans