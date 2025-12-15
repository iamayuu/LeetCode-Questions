class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return False
        dictnums2 = {}
        for index,i in enumerate(nums):
            if i in dictnums2:
                return True
            dictnums2[i]=index
        return False