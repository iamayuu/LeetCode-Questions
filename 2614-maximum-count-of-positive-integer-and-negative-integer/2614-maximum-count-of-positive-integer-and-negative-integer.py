class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        #Solution1 (Brute Force)
        # pos = 0
        # neg = 0
        # for n in nums:
        #     if n<0:
        #         neg+=1
        #     elif n>0:
        #         pos+=1
        # return max(pos,neg)

        #Solution2 (Optimization using Binary Search)
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right+1)//2
            if nums[mid]>=0:
                right = mid-1
            else:
                left = mid+1
        neg =left

        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right+1)//2
            if nums[mid]<=0:
                left = mid+1
            else:
                right = mid-1
        pos = len(nums)-left

        return max(pos,neg)