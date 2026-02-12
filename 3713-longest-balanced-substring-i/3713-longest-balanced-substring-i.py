class Solution:
    def longestBalanced(self, s: str) -> int:
        #Solution1 (Brute Force) [O(n^3) - TLE]
        # ans = 0
        # n= len(s)
        # for i in range(n):
        #     for j in range(i,n):
        #         subs = s[i:j+1]
        #         counter = Counter(subs)
        #         if len(set(counter.values()))==1:
        #             ans=max(ans, len(subs))
        # return ans

        #Solution 2
        ans = 0
        n= len(s)
        for i in range(n):
            counter = [0]*27
            for j in range(i,n):
                counter[ord(s[j])-ord('a')-1]+=1
                if len(set(counter))==2:
                    ans=max(ans, j-i+1)
        return ans                