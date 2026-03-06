class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        #Solution 1 
        # if len(s)<3:
        #     return True

        # for i in range(1,len(s)):
        #     if s[i]=="0" and "1" in s[i:]:
        #         return False
        # return True

        #Solution 2 
        if "01" in s:
            return False
        return True
        
                