class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # #Soltuion1 Brute Force
        # ans = 0
        # n = len(nums1)
        # m = len(nums2)
        # for i in range(n):
        #     for j in range(i,m):
        #         if nums1[i] <= nums2[j]:
        #             ans = max(ans, j-i)
        #         else:
        #             break
        # return ans

        #Solution 2 Using Binary Search for nums2 to find the farthest point
        # ans = 0
        # n = len(nums1)
        # m = len(nums2)
        # for i in range(n):
        #     left = i
        #     right = m-1
        #     j = 0
        #     while left<=right:
        #         mid = (left+right)//2
        #         if nums2[mid]<nums1[i]:
        #             #move left
        #             right=mid-1
        #         else:
        #             #move right storing the possible ans
        #             j=mid
        #             left = mid+1   
        #     ans = max(ans, j-i)
        # return ans

        #Solution 3 Using 2 Pointers
        ans = 0
        i, j = 0, 0
        n = len(nums1)
        m = len(nums2)
        while(i<n and j<m):
            if nums1[i] > nums2[j]:
                i+=1
            else:
                ans = max(ans, j-i)
                j+=1
        return ans
