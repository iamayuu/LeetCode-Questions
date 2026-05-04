class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        hmap = {}
        def dp(n,k):
            if n==k:
                return 1
            if n==0 or k==0:
                return 0
            if (n,k) in hmap:
                return hmap[(n,k)]
            hmap[(n,k)] = (dp(n-1,k-1) + (n-1)* dp(n-1,k))%((10**9)+7)
            return hmap[(n,k)]
        
        return dp(n,k)