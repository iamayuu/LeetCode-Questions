class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        if words[startIndex]==target:
            return 0
        #Solution1 
        # left = startIndex-1
        # right = startIndex+1
        # n=len(words)
        # ans = float("inf")
        # while left>-1:
        #     if words[left]==target:
        #         ans=min(ans, startIndex-left, abs(n-startIndex+left))
        #     left-=1
        
        # while right<n:
        #     if words[right]==target:
        #         ans=min(ans, right-startIndex, abs(n+startIndex-right))
        #     right+=1
        # return ans 

        #Solution2
        # ans = float("inf")
        # n=len(words)
        # for i in range(n):
        #     if words[i]==target:
        #         print(i)
        #         print(startIndex+n-i)
        #         ans = min(ans, abs(i-startIndex), abs(startIndex+n-i), abs(n-startIndex+i))
        # return ans 

        #Solution3 
        ans = float("inf")
        n=len(words)
        for i in range(n):
            if words[i]==target:
                print(i)
                print(startIndex+n-i)
                ans = min(ans, abs(i-startIndex), n-abs(i-startIndex))
        return ans 
