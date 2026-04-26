class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # mod = (10**9 +7)
        # if n&1==0:
        #     odd, even = n//2, n//2
        #     return (pow(5,even,mod)*pow(4,odd,mod))%mod
        # else:
        #     even = (n+1)//2
        #     odd = n//2
        #     return (pow(5,even,mod)*pow(4,odd,mod))%mod

        #More optimised
        mod = (10**9 +7)

        if n&1==0:
            # odd, even = n//2, n//2
            n1 = n//2
            return (pow(20,n1,mod))%mod
        else:
            # even = (n+1)//2
            # odd = n//2
            n1 = n//2
            return (pow(20,n1,mod)*5)%mod
