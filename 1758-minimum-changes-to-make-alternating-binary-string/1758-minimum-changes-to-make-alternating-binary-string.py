class Solution:
    def minOperations(self, s: str) -> int:
        #Solution1 (Brute Force)
        # if len(s)==1:
        #     return 0
        
        # count1 = 0
        # req1 = "1"
        # count2 = 0
        # req2 = "0"

        # for bit in s:
        #     if bit!=req1:
        #         count1 += 1
        #     if bit!=req2:
        #         count2 += 1
        #     req1="0" if req1=="1" else "1"
        #     req2="0" if req2=="1" else "1"
        
        # return min(count1,count2)

        #Solution2 (Bit more optimal from soln 1)
    
        count = 0
        req = "1"

        for bit in s:
            if bit!=req:
                count += 1
            req="0" if req=="1" else "1"
        
        return min(count,len(s)-count)
        
