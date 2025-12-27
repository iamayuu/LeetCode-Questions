class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution1 (Brute Force - Complexity is O(k*n))
        # for i in range(k):
        #     temp = nums[len(nums)-1]
        #     nums[:]=[temp]+nums[:len(nums)-1]

        #Solution 2 (normalizing the k and slicing it)
        # if k>len(nums):
        #     k=k%len(nums)
        # nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]

        #Solution3 (Reversing the array)
        if k>len(nums):
            k=k%len(nums)        
        nums.reverse()
        nums[:]=nums[k-1::-1]+nums[-1:k-1:-1]

