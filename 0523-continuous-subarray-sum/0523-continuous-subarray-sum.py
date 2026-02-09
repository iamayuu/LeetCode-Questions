class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #Solution1 (Brute Force) [Time - O(n^2)]
        # n = len(nums)
        # for i in range(n-1):
        #     sum=nums[i]
        #     for j in range(i+1,n):
        #         sum+=nums[j]
        #         if sum%k==0:
        #             return True
        # return False

        #Solution2
        hashMap = dict()
        hashMap[0] = -1
        sum = 0
        for i,n in enumerate(nums):
            sum += n
            if sum % k in hashMap:
                length = i-hashMap[sum%k]
                if length >=2:
                    return True
            else:
                hashMap[sum%k]=i
        return False