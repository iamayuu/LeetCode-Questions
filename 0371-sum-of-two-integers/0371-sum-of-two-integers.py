class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (mask&b)>0:
            sum = a^b
            carry = a&b
            a,b = sum, carry<<1
        return (mask&a) if b>0 else a
