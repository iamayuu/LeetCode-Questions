class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            total_current = numbers[left]+numbers[right]
            if target == total_current:
                return [left+1,right+1]
            else:
                if target<total_current:
                    right-=1
                else:
                    left+=1