class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #Solution1 (Brute Force - TLE)
        # total = 0xffffffff
        # while left<=right:
        #     total &=left
        #     left+=1
        # return total

        #Solution2 (Optimised)
        zeroes_lost = 0
        while left!=right:
            left = left>>1
            right = right>>1
            zeroes_lost+=1
        return left<<zeroes_lost
