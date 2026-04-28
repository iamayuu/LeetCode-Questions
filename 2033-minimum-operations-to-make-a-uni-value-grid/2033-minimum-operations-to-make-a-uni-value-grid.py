class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #Solution1 BruteForce
        m = len(grid)
        n = len(grid[0])
        nums = []
        for item in grid:
            for num in item:
                nums.append(num)
        
        nums.sort()
        ans = 0
        total = m*n
        if total&1==0:
            #even
            mid = nums[total//2]
            for num in nums:
                if num%x != mid%x:
                    return -1
                else:
                    ans += (abs(mid-num))//x
        else:
            #odd
            mid = nums[total//2]
            for num in nums:
                if num%x != mid%x:
                    return -1
                else:
                    ans += (abs(mid-num))//x
        
        return ans