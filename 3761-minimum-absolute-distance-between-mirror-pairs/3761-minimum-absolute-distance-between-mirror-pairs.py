class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        #Solution1 Brute Force -  TLE
        # n = len(nums)
        # ans = float("inf")
        # for i in range(n-1):
        #     num = nums[i]
        #     rev_s=""
        #     for s in str(num):
        #         rev_s = s+rev_s
        #     rev_num=int(rev_s)
        #     j=i+1
        #     while j<n:
        #         if nums[j]==rev_num:
        #             ans = min(ans, abs(i-j))
        #         j+=1
        # return -1 if ans == float("inf") else ans

        #Solution2 
        n = len(nums)
        ans = float("inf")
        hmap = dict()
        for i in range(n):
            num = nums[i]
            if num in hmap:
                ans = min(ans, i-hmap[num])
            rev_s=str(num)[::-1]
            rev_num=int(rev_s)
            hmap[rev_num]=i
        return -1 if ans == float("inf") else ans
