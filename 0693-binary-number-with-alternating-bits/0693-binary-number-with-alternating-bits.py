class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        #Solution1 (Brute Force)
        # crr_check = n&1
        # while n!=0:
        #     n=n>>1
        #     if n&1 == crr_check:
        #         return False
        #     crr_check=n&1
        # return True

        #Solution2 (Using bit manipulation)
        return n&(n>>1)==0 and (n^(n>>1))&((n^(n>>1))+1)==0   