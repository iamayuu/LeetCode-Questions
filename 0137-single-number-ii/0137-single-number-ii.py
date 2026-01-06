class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Solution1 (Brute Force)
        # from collections import Counter
        # freq = Counter(nums)
        # return freq.most_common()[-1][0]

        #Solution2 (Using Bit Manipulation)
        ans=0
        for i in range(32):
            count = 0
            for n in nums:
                n=n&0xffffffff
                if (n>>i)&1==1:
                    count+=1
            if count%3==1:
                ans = ans | (1<<i)
        return ans if ans<2**31 else ans-2**32