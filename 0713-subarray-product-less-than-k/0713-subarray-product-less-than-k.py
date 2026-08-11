class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #brute force [O(n^2)]
        # n = len(nums)
        # count = 0
        # for i in range(n):
        #     product = 1
        #     for j in range(i,n):
        #         product = product*nums[j]
        #         if product < k:
        #             count+=1
        #         else:
        #             break
        # return count

        #Sliding Window
        import math
        n = len(nums)
        l = 0
        r = 0
        product = nums[l]
        count = 0
        while r<n and l<n:
            if product<k:
                count+=(r-l+1)
                r+=1
                if r<n:
                    product=product*nums[r]
            else:
                product=product//nums[l]
                l+=1
        return count