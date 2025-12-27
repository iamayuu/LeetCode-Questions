class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Solution1 (Using HSet)
        # my_set = set()
        # i=0
        # while i<len(nums):
        #     #print(f" i: {i} number: {nums[i]}")
        #     if nums[i] in my_set:
        #         del nums[i]
        #     else:
        #         my_set.add(nums[i])
        #         i+=1
        # return len(my_set)

        #Solution2 (Uaing 2 pointers)
        k=0
        for i in range(1,len(nums)):
            if nums[k]!=nums[i]:
                nums[k+1]=nums[i]
                k+=1
        return k+1


