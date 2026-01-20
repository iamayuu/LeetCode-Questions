class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        #Solution1 (Brute Force)
        ans = []
        for n in nums:
            value = -1
            for i in range(1, n):
                if i | (i+1) == n:
                    value = i
                    break
            ans.append(value)
        return ans