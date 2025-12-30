class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Solution1 (BruteForce to find n/2 elements)
        n1=0
        n2=0
        n = len(nums1)+len(nums2)
        mid = int(n/2)
        i = 0
        mid_value1 =0
        mid_value2 =0
        print(mid)
        while i<=mid :
            value = 0
            print(f"i: {i}, n1: {n1}, n2: {n2}")
            if n1<len(nums1):
                if n2<len(nums2):
                    if nums1[n1]<=nums2[n2]:
                        value=nums1[n1]
                        n1+=1
                    else:
                        value=nums2[n2]
                        n2+=1
                else:
                    value=nums1[n1]
                    n1+=1
            else:
                value=nums2[n2]
                n2+=1
            if i==mid-1:
                mid_value1 = value
            elif i==mid:
                mid_value2 = value           
            i+=1
        if n%2==0:
            return (mid_value1+mid_value2)/2.0
        else:
            return mid_value2