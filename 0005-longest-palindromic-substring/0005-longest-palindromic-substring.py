class Solution:
    def longestPalindrome(self, s: str) -> str:
        #BruteForce - get all the strings, check if palindrome if yes cal length and ans store
        n = len(s)
        ans = s[0]
        for i in range(n-1):
            for j in range(i+1,n):
                test = s[i:j+1]
                if test==test[::-1]:
                    if len(test)>len(ans):
                        ans = test

        return ans
