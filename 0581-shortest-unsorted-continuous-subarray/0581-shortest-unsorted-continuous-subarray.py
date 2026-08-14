class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # #Solution 1
        # n = len(nums)
        # sorted_nums = sorted(nums)
        # l, r = 0, n-1
        # while l<n:
        #     if nums[l]==sorted_nums[l]:
        #         l+=1
        #     else:
        #         break
        # while r>-1:
        #     if nums[r]==sorted_nums[r]:
        #         r-=1
        #     else:
        #         break
        
        # return 0 if r<l else (r-l+1)

        # #Solution1 optimized
        # n = len(nums)
        # sorted_nums = sorted(nums)
        # l, r = 0, n-1
        # while l<r:
        #     if nums[l]==sorted_nums[l]:
        #         l+=1
        #     elif nums[r]==sorted_nums[r]:
        #         r-=1
        #     else:
        #         break
        
        # return 0 if r==l else (r-l+1)

        n = len(nums)
        if n<=1:
            return  0
        left , right = n-1, 0
        smallest,largest = float("inf"), float("-inf")

        #finding the furthest point from right to left that is unsorted
        for i in range(n-1,-1,-1):
            if nums[i]<=smallest:
                smallest = nums[i]
            else:
                left = i
        #finding the furthest point from left to right that is unsorted
        for i in range(n):
            if nums[i]>=largest:
                largest = nums[i]
            else:
                right = i

        return right-left+1 if right-left+1 > 0  else 0