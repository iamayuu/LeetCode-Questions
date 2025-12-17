class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solution 1
        # prefix_multi = [1]*len(nums)
        # suffix_multi = [1]*len(nums)
        # result = []
        
        # for i in range(len(nums)):
        #     if i>0:
        #         prefix_multi[i]=prefix_multi[i-1] * nums[i-1]
        #         suffix_multi[len(nums)-1-i]=suffix_multi[len(nums)-i]*nums[len(nums)-i]
        
        # for i in range(len(nums)):
        #     result.append(prefix_multi[i]*suffix_multi[i])

        # return result

        #Solution 2
        result = [1]*len(nums)
        suffix_multi = 1
        for i in range(1,len(nums)):
            result[i]=result[i-1] * nums[i-1]

        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*suffix_multi
            suffix_multi=suffix_multi*nums[i]
                
        return result