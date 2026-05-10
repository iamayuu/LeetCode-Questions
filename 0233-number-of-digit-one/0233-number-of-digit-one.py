class Solution:
    def countDigitOne(self, n: int) -> int:
        #Solution1 Brute Force
        # count = 0
        # for i in range(n+1):
        #     num = i
        #     while num>0:
        #         if num%10==1:
        #             count+=1
        #         num=num//10
        # return count

        #Solution 2 
        ans = 0
        i = 1
        while i <= n:
            prefix = n // (i * 10)
            curr = (n // i) % 10
            suffix = n % i
            
            if curr == 0:
                ans += prefix * i
            elif curr == 1:
                ans += prefix * i + suffix + 1
            else:
                ans += (prefix + 1) * i
            
            # Move to the next digit (tens, hundreds, etc.)
            i *= 10
            
        return ans