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
        and_check = (n&(n>>1)==0)
        xor = n^(n>>1)
        xor_check = (xor&(xor+1)==0)

        return and_check and xor_check