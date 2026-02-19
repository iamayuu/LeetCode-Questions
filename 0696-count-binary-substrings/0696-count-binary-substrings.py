class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #Solution1 (Brute Force)
        # n = len(s)
        # ans = 0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         substring = s[i:j+1]
        #         m = len(substring)
        #         if m%2==0:
        #             s1 = substring[:m//2]
        #             s2 = substring[m//2:]
        #             s1_flipped = ''.join('1' if c == '0' else '0' for c in s1)
        #             if s1_flipped==s2 and (int(s1,2)==0 or int(s2,2)==0):
        #                 ans+=1
        # return ans

        #Solution2
        prev = 0
        crr = 1
        ans = 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                crr+=1
            else:
                ans+=min(prev,crr)
                prev = crr
                crr=1
        ans+=min(prev,crr) #for last set
        return ans
