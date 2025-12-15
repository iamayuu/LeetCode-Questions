class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictHashMap = {}
        for i in range(len(nums)):
            intComplementNum = target-nums[i]
            if intComplementNum in dictHashMap:
                return [dictHashMap[intComplementNum], i]
            else:
                dictHashMap[nums[i]]=i