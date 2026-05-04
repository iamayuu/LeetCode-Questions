class Solution:
    def countPrimes(self, n: int) -> int:
        #Solution1 Brute Force
        # def is_prime(num):
        #     if num==1:
        #         return False
        #     if num==2 or num==3:
        #         return True
        #     for i in range(2,(num//2)+1):
        #         if num%i==0:
        #             return False
        #     return True
        # count=0
        # for i in range(1,n):
        #     if is_prime(i):
        #         count+=1
        # return count

        #Solution 2 Sieve of Eratosthenes
        # The Sieve of Eratosthenes is an ancient, efficient algorithm for finding all prime numbers up to a specified integer \(n\). It works by creating a list of numbers from 2 to \(n\), then iteratively marking the multiples of each prime number as composite (starting with 2), leaving only primes behind. It has a time complexity of \(O(n \log \log n)\)
        # if n<=1:
        #     return 0
        # arr = [True]*(n)
        # arr[0], arr[1] = False, False
        # count=0
        # num=2
        # while num<n:
        #     if arr[num]:
        #         count+=1
        #     for i in range(num*2,n,num):
        #         arr[i]=False
        #     num+=1
        # return count

        #Solution 3 more optimised of 2

        if n<=1:
            return 0
        arr = [True]*(n)
        arr[0], arr[1] = False, False

        num=2
        while num*num<n:
            if arr[num]:
                for i in range(num*num,n,num):
                    arr[i]=False
            num+=1
        return sum(arr)