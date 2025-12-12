class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictHeap = {}
        for i in range(len(nums)):
            if target-nums[i] in dictHeap:
                return [dictHeap[target-nums[i]],i]
            else:
                dictHeap[nums[i]]=i
        return []