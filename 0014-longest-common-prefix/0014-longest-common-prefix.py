class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = min(strs)
        b = max(strs)
        ans = ""
        i=0
        while i<len(a) and a[i]==b[i]:
            ans = ans+a[i]
            i +=1
        return ans
