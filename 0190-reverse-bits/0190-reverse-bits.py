class Solution:
    def reverseBits(self, n: int) -> int:
        #Solution1 (Brute Force)
        # binary = ""
        # while n>0:
        #     binary=str(n%2)+binary
        #     n=n//2
        # binary = binary.zfill(32) #Making it 32 bit
        # #Now we will need to reverse it to get desired binary and reverse again to get desired number of that binary
        # offset=1
        # ans = 0
        # for i in binary:
        #     ans = ans+(int (i)*offset)
        #     offset*=2
        # return ans

        #Solution 2 (Using Bit Manipulation)
        result = 0
        #Using a loop for 32 bits
        for _ in range(32):
            last_bit = n&1 #Gets the rightmost bit of n
            result = result << 1 #Creates empty bit space in right of result
            result = result | last_bit #Appends the lastbit (replaces the space by our value)
            n=n>>1
        return result