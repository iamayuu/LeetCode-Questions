class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = 0, 0
        
        nums = []
        while r<n and l<m:
            if nums1[l]<=nums2[r]:
                nums.append(nums1[l])
                l+=1
            else:
                nums.append(nums2[r])
                r+=1
        while r<n:
            nums.append(nums2[r])
            r+=1

        while l<m:
            nums.append(nums1[l])
            l+=1
        
        nums1[:]=nums