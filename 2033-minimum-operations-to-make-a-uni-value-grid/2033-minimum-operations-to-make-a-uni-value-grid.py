class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #Solution1 BruteForce
        nums = []
        for item in grid:
            for num in item:
                nums.append(num)
        
        nums.sort()
        ans = 0
        total = len(nums)
        mid = nums[total//2]
        base =  mid%x
        for num in nums:
            if num%x !=base:
                return -1
            else:
                ans += (abs(mid-num))//x
        
        return ans