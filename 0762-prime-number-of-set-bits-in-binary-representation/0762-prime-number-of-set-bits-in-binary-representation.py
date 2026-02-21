class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_nums = {2,3,5,7,11,13,17,19}
        ans = 0
        while left<=right:
            temp = left
            count=0
            while temp>0:
                temp = temp&(temp-1)
                count+=1
            if count in prime_nums:
                ans+=1
            left+=1
        return ans