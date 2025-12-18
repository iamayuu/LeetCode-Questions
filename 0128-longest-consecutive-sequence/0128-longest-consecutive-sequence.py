class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        max_length = 1
        current_length = 1
        n = nums[0]
        for i in range(1, len(nums)):
            if nums[i]==n+1:
                n = nums[i]
                current_length +=1
            elif nums[i]==n:
                n = nums[i]
            else:
                current_length=1
                n = nums[i]
            if current_length >= max_length:
                max_length=current_length


        return max_length


