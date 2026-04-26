class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i,num in enumerate(nums):
            if target-num in hmap:
                return [hmap[target-num] , i]
            hmap[num]=i
