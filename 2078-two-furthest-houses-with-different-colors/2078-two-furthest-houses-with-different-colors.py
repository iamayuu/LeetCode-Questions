class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #Solution1 BruteForce
        # ans = 0
        # n = len(colors)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if colors[i] != colors[j]:
        #             ans = max(ans, j-i)
        # return ans

        #Solution2 
        ans = 0
        n = len(colors)
        left = colors[0]
        right = colors[n-1]
        for i in range(n-1,0,-1):
            if colors[i] != left:
                ans = max(ans, i)
                break
        for i in range(n-1):
            if colors[i] != right:
                ans = max(ans, n-1-i)
                break
        return ans