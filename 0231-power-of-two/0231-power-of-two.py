class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Solution1 (Brute Force)
        # if n<=0:
        #     return False
        # while n>1:
        #     if n%2==1:
        #         return False
        #     n=n//2
        # return True

        #Solution2 (using bit wise operation)
        return n&(n-1)==0 if n>0 else False