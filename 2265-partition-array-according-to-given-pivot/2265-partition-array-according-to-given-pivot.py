class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #Solution 1 Brute Force
        # ans = []
        # i = 0
        # n = len(nums)
        # while i<n:
        #     if nums[i]<pivot:
        #         ans.append(nums[i])
        #     i+=1
        # i=0
        # while i<n:
        #     if nums[i]==pivot:
        #         ans.append(nums[i])
        #     i+=1
        # i=0
        # while i<n:
        #     if nums[i]>pivot:
        #         ans.append(nums[i])
        #     i+=1
        # return ans
        
        #Solution 2 Two Pointers
        # n = len(nums)
        # ans = [pivot]*n
        # left = 0
        # right = n-1
        # for i in range(n):
        #     if nums[i]<pivot:
        #         ans[left]=nums[i]
        #         left+=1
        #     if nums[n-1-i]>pivot:
        #         ans[right]=nums[n-1-i]
        #         right-=1
        # return ans

        #Solution 3 using extra space
        less, equal, great = [], [], []
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                great.append(num)
        return less+equal+great