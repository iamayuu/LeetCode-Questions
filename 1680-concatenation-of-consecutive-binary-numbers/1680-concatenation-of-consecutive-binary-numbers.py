class Solution:
    def concatenatedBinary(self, n: int) -> int:
        str = ""
        for num in range(1,n+1):
            str = str+bin(num)[2:]
        
        ans = (int(str,2))%((10**9)+7)
        return ans