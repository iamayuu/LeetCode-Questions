class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Solution1 (Bit Manipualtion)
        #Using property -> n^n=0 and n^0=n, any dulicate will become 0 and unique will stay
        return reduce(lambda x,y: x^y, nums)