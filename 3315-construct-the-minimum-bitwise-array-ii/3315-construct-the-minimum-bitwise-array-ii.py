class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        #Solution1 (Brute Force) [TC - O(n*m) SC- O(1)]
        # ans = []
        # for n in nums:
        #     value = -1
        #     for i in range(1, n):
        #         if i | (i+1) == n:
        #             value = i
        #             break
        #     ans.append(value)
        # return ans

        #Solution2 (Optimized) [TC - O(n), SC - O(1) if we dont consider ans list]
        ans = []
        for n in  nums:
            if n == 2:
                ans.append(-1)
                continue
            for i in  range(32):
                #check for fist unset bit
                if n & (1<<i)==0:
                    #prev_bit = i-1
                    #make prev_bit 0
                    value = n & ~(1<<(i-1))
                    ans.append(value)
                    break
        return ans
