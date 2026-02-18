class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        crr_check = n&1
        while n!=0:
            n=n>>1
            if n&1 == crr_check:
                return False
            crr_check=n&1
        return True