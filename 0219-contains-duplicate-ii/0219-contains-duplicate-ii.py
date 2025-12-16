
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictHashMap = {}
        for index, i in enumerate(nums):
            if i in dictHashMap and abs(dictHashMap[i]-index)<=k:
                return True
            dictHashMap[i]=index

        return False