class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = str.lower(s)

        return s==s[::-1]

