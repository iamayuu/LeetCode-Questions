class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = str.lower(s)

        start = 0
        end = len(s)-1

        for i in range(int(len(s)/2)):
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True

