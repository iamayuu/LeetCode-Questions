class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Solution1 (BruteForce to find n/2 elements) [Time - O(n+m), Space - O(1)]
        # n1 = 0
        # n2 = 0
        # n = len(nums1) + len(nums2)
        # mid = int(n / 2)
        # i = 0
        # mid_value1 = 0
        # mid_value2 = 0
        # print(mid)
        # while i <= mid:
        #     value = 0
        #     print(f"i: {i}, n1: {n1}, n2: {n2}")
        #     if n1 < len(nums1):
        #         if n2 < len(nums2):
        #             if nums1[n1] <= nums2[n2]:
        #                 value = nums1[n1]
        #                 n1 += 1
        #             else:
        #                 value = nums2[n2]
        #                 n2 += 1
        #         else:
        #             value = nums1[n1]
        #             n1 += 1
        #     else:
        #         value = nums2[n2]
        #         n2 += 1
        #     if i == mid - 1:
        #         mid_value1 = value
        #     elif i == mid:
        #         mid_value2 = value
        #     i += 1
        # if n % 2 == 0:
        #     return (mid_value1 + mid_value2) / 2.0
        # else:
        #     return mid_value2

        #Solution2 (Using Binary Search) 
        #Getting the smaller array into nums1
        import sys
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        mid = (n1+n2+1)//2
        start = 0
        end = n1
        while start<=end:
            mid1 = (start+end)//2
            mid2 = mid-mid1

            l1 = float("-inf") if mid1==0 else nums1[mid1-1]
            r1 = float("inf") if mid1==n1 else nums1[mid1]
            l2 = float("-inf") if mid2==0 else nums2[mid2-1]
            r2 = float("inf") if mid2==n2 else nums2[mid2]
                     
            if mid2<len(nums2):
                r2 = nums2[mid2]

            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                end=mid1-1
            else:
                start=mid1+1
        





