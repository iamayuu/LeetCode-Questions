class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Solution 1 (using sum formula)
        # n = len(nums)
        # total_sum = (n*(n+1))/2
        # my_sum = 0
        # for n in nums:
        #     my_sum +=n

        # return int(total_sum-my_sum)

        #Solution 2 (Using XOR operation)
        # ans = 0
        # for n in nums:
        #     ans = ans^n
        # for n in range(len(nums)+1):
        #     ans = ans^n
        # return ans

        #Solutio 3 (Using sorting and indexs to match)
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)

