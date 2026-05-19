class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if nums1[n-1]<nums2[0]:
            return -1
        if nums2[m-1]<nums1[0]:
            return -1
        
        i, j = 0, 0
        while i<n and j<m:
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1