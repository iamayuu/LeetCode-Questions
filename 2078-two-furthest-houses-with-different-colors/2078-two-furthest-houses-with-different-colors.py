class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #Solution1 BruteForce
        ans = 0
        n = len(colors)
        for i in range(n-1):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    ans = max(ans, j-i)
        return ans