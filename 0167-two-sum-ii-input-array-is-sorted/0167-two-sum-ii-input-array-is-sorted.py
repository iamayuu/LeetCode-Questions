class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            if target-num in numbers:
                return [numbers.index(num)+1,len(numbers)-1-numbers[::-1].index(target-num)+1]
