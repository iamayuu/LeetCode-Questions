class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Solution 1 (using hashmap for unqiue elements)
        # if len(nums)<2:
        #     return False
        # dictnums2 = {}
        # for index,i in enumerate(nums):
        #     if i in dictnums2:
        #         return True
        #     dictnums2[i]=index
        # return False

        #Solution 2 (using sort and compare next element)
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
            
        # return False

        #Solution 3 (using set and cehck existance)
        nums_set = set()

        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False