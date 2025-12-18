class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution 1 (Time = O(n log n))
        # if nums == []:
        #     return 0
        # nums.sort()
        # max_length = 1
        # current_length = 1
        # n = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i]==n+1:
        #         n = nums[i]
        #         current_length +=1
        #     elif nums[i]==n:
        #         n = nums[i]
        #     else:
        #         current_length=1
        #         n = nums[i]
        #     if current_length >= max_length:
        #         max_length=current_length

        # return max_length

        #Solution 2 (Time = O(n))
        if nums == []:
            return 0        
        my_set = set(nums)
        max_length = 1
        for num in my_set: 
            if num-1 not in my_set:
                i=1
                while num+i in my_set:
                    i+=1
                max_length=max(i,max_length)
        
        return max_length


