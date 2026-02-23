class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        max_bin_codes = 1<<k  # max possible is 2 power k
        #Early termination condition
        if n-k+1<max_bin_codes:
            return False

        unique_substr = set()
        for i in range(n-k+1):
            substr = s[i:i+k]
            if substr not in unique_substr:
                unique_substr.add(substr)
        return len(unique_substr)==max_bin_codes
