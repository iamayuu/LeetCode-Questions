class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num<=1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        min_diff = float("inf")
        res = [-1,-1]
        last = 0
        for i in range(left, right+1):
            if isPrime(i):
                if last!=0:
                    diff = i-last
                    if diff<min_diff:
                        min_diff=diff
                        res = [last,i]
                        if diff==2:
                            return res
                last = i
                
        return res
                
                    

                    