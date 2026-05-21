class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #Brute Force
        # def prefix(num1,num2):
        #     str1 = str(num1)
        #     str2 = str(num2)
        #     p=0
        #     while p<len(str1) and p<len(str2):
        #         if str1[p]==str2[p]:
        #             p+=1
        #         else:
        #             break
        #     return p
        # ans = 0
        # for num1 in arr1:
        #     for num2 in arr2:
        #         ans = max(ans,prefix(num1,num2))
        # return ans

        #Using hashset
        prefixes = set()
        for num1 in arr1:
            str1=str(num1)
            pfx = ""
            for s in str1:
                pfx+=s
                if pfx not in prefixes:
                    prefixes.add(pfx)
        
        ans = 0
        for nums2 in arr2:
            str2=str(nums2)
            pfx = ""
            for s in str2:
                pfx+=s
                if pfx in prefixes:
                    ans = max(ans,len(pfx))
                else:
                    break
        return ans