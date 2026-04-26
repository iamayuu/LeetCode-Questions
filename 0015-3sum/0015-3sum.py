class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums.sort()
        # print(nums)
        # n = len(nums)
        # ans = []
        # i=0
        # while i<n and nums[i]<1:
        #     if i>0 and nums[i]==nums[i-1]:
        #         i+=1
        #         continue
        #     l = i+1
        #     r = n-1
        #     while l<r:
        #         if nums[i]+nums[l]+nums[r]==0:
        #             ans.append([nums[i],nums[l],nums[r]])
        #             l+=1
        #             r-=1
        #             while nums[l]==nums[l-1] and l<r:
        #                 l+=1
        #         elif nums[i]+nums[l]+nums[r] >0:
        #             r-=1
        #         elif nums[i]+nums[l]+nums[r] < 0:
        #             l+=1
            
        #     i+=1
            
        # return ans

        #Clean Shit
        nums.sort()
        n = len(nums)
        ans = []

        i=0
        while i<n and nums[i]<1:
            
            #Skipping the duplicate first number as they will give repeated outputs
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue

            l = i+1
            r = n-1

            while l<r:

                threesum = nums[i]+nums[l]+nums[r]
                
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
            
            i+=1
            
        return ans