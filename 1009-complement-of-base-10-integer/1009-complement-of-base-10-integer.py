class Solution:
    def bitwiseComplement(self, n: int) -> int:
        #Solution 1 (Brute Force)
        if n==0:
            return 1
        s=""
        while n>0: 
            last_bit = n&1
            if last_bit==0:
                s="1"+s
            else:
                s="0"+s
            n=n>>1
        return int(s,2)