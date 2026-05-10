class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]
        # nums.sort()
        
        # for i in range(1,len(nums),3):
        #     if nums[i]!=nums[i-1]:
        #         return nums[i-1]
        # return nums[-1]

        count = dict()
        for n in nums:
            if n not in count:
                count[n]=1
            else:
                count[n]+=1
        
        for k,v in count.items():
            if v==1:
                return k