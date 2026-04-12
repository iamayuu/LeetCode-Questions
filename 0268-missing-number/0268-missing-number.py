class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        last = -1
        for n in nums:
            if last+1==n:
                last=n
            else:
                return last+1
        return last+1