class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num<=9:
                ans.append(num)
            else:
                num_s = str(num)
                for digits in num_s:
                    ans.append(int(digits))
        return ans
