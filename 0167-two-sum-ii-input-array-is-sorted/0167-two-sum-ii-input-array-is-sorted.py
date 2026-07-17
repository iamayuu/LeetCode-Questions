class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #brute force
        # n = len(numbers)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]

        # return [0,1]

        #Optimal
        hmap = dict()
        n = len(numbers)
        for i in range(n):
            num = numbers[i]
            if target-num in hmap:
                return [hmap[target-num]+1, i+1]
            if num not in hmap:
                hmap[num]=i
        
        return [0,1]