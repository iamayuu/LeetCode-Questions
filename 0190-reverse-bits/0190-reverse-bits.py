class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        while n>0:
            bit = n%2
            n=n//2
            binary = str(bit)+binary
        binary = binary.zfill(32)

        offset = 1
        res = 0
        for bit in binary:
            res+= int(bit)*offset
            offset*=2
        return res