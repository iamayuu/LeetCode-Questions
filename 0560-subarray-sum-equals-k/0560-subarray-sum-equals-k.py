class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i]+prefix_sum[i-1])
        
        hashMap = {}
        count = 0
        for j in range(len(prefix_sum)):
            diff = prefix_sum[j]-k
            if diff == 0:
                count+=1
            if diff in hashMap:
                count+=hashMap[diff]
            
            if prefix_sum[j] in hashMap:
                hashMap[prefix_sum[j]]+=1
            else:
                hashMap[prefix_sum[j]]=1

        return count