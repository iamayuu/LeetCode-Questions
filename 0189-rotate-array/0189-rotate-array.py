class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution1 Brute Force (fast but taking space)
        # n=len(nums)
        # k=k%n
        # nums1 = nums[:n-k]
        # nums2=nums[n-k:]
        # nums[:]=nums2+nums1

        #Solution2 better space then solution 1
        # n=len(nums)
        # k=k%n
        # nums[:] = nums[n-k:]+nums[:n-k]
        

        #Solution3 same time best space
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
