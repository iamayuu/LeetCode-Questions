class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        two_power_tracker = 1

        for i in range(1,n+1):
            if two_power_tracker*2==i:
                two_power_tracker=i

            ans[i]=ans[i-two_power_tracker]+1

        return ans