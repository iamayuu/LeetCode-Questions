class Solution:
    def minOperations(self, s: str) -> int:
        #Solution1 (Brute Force)
        if len(s)==1:
            return 0
        
        count1 = 0
        req = "1"
        for bit in s:
            if bit!=req:
                count1 += 1
            req="0" if req=="1" else "1"
        
        count2 = 0
        req = "0"
        for bit in s:
            if bit!=req:
                count2 += 1
            req="0" if req=="1" else "1"
        
        return min(count1,count2)
        
