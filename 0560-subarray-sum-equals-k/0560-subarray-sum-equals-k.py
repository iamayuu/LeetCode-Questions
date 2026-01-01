class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Solution1 (Brute Force) [Time - O(n^2)]
        # total_subarray = 0
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i, len(nums)):
        #         sum+=nums[j]
        #         if sum==k:
        #             total_subarray+=1
        # return total_subarray

        #Solution2 (Optimal Time)
        # total_subarray = 0

        # #Array Pre-Processing
        # prefix_sum = []
        # curr_sum=0
        # for n in nums:
        #     curr_sum+=n
        #     prefix_sum.append(curr_sum)
        # counter = {}
        # #Finding subarray with sum k and calculating counters
        # for curr_psum in prefix_sum:
        #     if curr_psum-k==0:
        #         total_subarray+=1
        #     if curr_psum-k in counter:
        #         total_subarray+=counter[curr_psum-k]
        #     if curr_psum in counter:
        #         counter[curr_psum]+=1
        #     else:
        #         counter[curr_psum]=1

        # return total_subarray

        #Solution3 (Optiomal Time and Space)
        hashMap = {} #For storing counter
        hashMap[0]=1 #Adding for running_sum-k==0 condition
        running_sum = 0
        total_subarray = 0
        for n in nums:
            running_sum+=n
            if running_sum-k in hashMap:
                total_subarray+=hashMap[running_sum-k]
            if running_sum in hashMap:
                hashMap[running_sum]+=1
            else:
                hashMap[running_sum]=1
        return total_subarray