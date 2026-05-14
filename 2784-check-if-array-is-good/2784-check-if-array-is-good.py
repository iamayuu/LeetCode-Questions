class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxNum = max(nums)
        n = len(nums)
        if n!=maxNum+1:
            return False
        
        if nums.count(maxNum)!=2:
            return False
        
        return len(set(nums))==maxNum