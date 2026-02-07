class Solution:
    def minimumDeletions(self, s: str) -> int:
        #Solution1 (Array Preprocessing)
        n = len(s)
        #Array preprocessing - count how many a to right of an index and how many B to left of index
        # a_right = [0]*n
        # a_count = 0
        # for i in range(n-1, -1, -1):
        #     a_right[i] = a_count
        #     if s[i] == 'a':
        #         a_count+=1

        # b_left = [0]*n
        # b_count = 0
        # for i in range(n):
        #     b_left[i] = b_count
        #     if s[i] == 'b':
        #         b_count+=1

        # ans = float("inf")
        # for i in range(n):
        #     ans = min(ans, a_right[i]+ b_left[i])
        # return ans

        #Solution2 (Using Stack - LIFO)
        # stack = []
        # count = 0
        # n = len(s)
        # for i in range(n):
        #     if s[i]=='a':
        #         if stack and stack[-1]=='b':
        #             stack.pop()
        #             count+=1
        #         else:
        #             stack.append('a')
        #     else:
        #         stack.append('b')
        # return count

        #Solution3 (Optimised Space of Solution 1)
        # n = len(s)
        # #Array preprocessing - count how many a to right of an index 
        # a_right = [0]*n
        # a_count = 0
        # for i in range(n-1, -1, -1):
        #     a_right[i] = a_count
        #     if s[i] == 'a':
        #         a_count+=1
        
        # ans = float("inf")
        # b_count=0
        # for i in range(n):
        #     ans = min(ans,a_right[i]+b_count)
        #     if s[i]=='b':
        #         b_count+=1
        
        # return ans

        #Soltuion 4 (More Optimized Space Solution 3 and Solution 1)
        n = len(s)
        #Array preprocessing - count how many total a in the string
        a_count = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'a':
                a_count+=1
        
        ans = float("inf")
        b_count=0
        for i in range(n):
            if s[i]=='a':
                a_count -= 1
            ans = min(ans,a_count+b_count)
            if s[i]=='b':
                b_count+=1

        return ans        