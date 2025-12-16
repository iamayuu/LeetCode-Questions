class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        needle_size = len(needle)
        for i in range(len(haystack)):
            check_string = haystack[i:i+needle_size]
            if check_string==needle:
                return i

        return -1