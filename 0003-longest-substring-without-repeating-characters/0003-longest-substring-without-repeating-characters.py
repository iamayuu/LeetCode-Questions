class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Solution1 (BruteForce) [Time - O(n^2)]
        # max_len = 0
        # for i in range(len(s)):
        #     substr = ""
        #     for j in range(i,len(s)):
        #         if s[j] not in substr:
        #             substr+=s[j]
        #             max_len = max(max_len, len(substr))
        #         else:
        #             substr=""
        # return max_len

        #Solution2 (Using 2 Pointers Sliding Window)
        max_len=0
        l, r = 0, 0
        HashMap = {} #To Store letter and their last index
        while r< len(s):
            if s[r] not in HashMap or HashMap[s[r]]<l:
                HashMap[s[r]]=r
                length = r-l+1
                max_len=max(max_len, length)
            else:
                l = HashMap[s[r]]+1
                HashMap[s[r]]=r
            r+=1
        return max_len