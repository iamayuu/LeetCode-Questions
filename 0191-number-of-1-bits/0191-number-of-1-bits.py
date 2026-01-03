class Solution:
    def hammingWeight(self, n: int) -> int:
        #Solution1 (Brute Force)
        # binary = ""
        # while n>0:
        #     binary = str(n%2)+binary
        #     n = n//2
        # result = 0
        # for b in binary:
        #     if b=='1':
        #         result+=1
        # return result

        #Solution2 (Brute Force - Optimized)
        result = 0
        while n>0:
            if n%2==1:
                result+=1
            n = n//2
        return result