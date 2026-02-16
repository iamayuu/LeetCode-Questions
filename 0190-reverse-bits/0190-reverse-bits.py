class Solution:
    def reverseBits(self, n: int) -> int:
        #Brute Force
        # binary = ""
        # while n>0:
        #     bit = n%2
        #     n=n//2
        #     binary = str(bit)+binary
        # binary = binary.zfill(32)

        # offset = 1
        # res = 0
        # for bit in binary:
        #     res+= int(bit)*offset
        #     offset*=2
        # return res

        #Optimized
        res = 0
        for i in range(32):
            check_bit = n&(1<<i)
            if check_bit:
                res = res|(1<<(31-i))
            else:
                res=res&~(1<<(31-i))
        return res