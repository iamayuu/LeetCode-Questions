class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        #Solution1 Brute Force
        ans = []
        hash = dict()
        arr.sort()
        for num in arr:
            count = num.bit_count()
            if count in hash:
                hash[count].append(num)
            else:
                hash[count]=[num]

        return [item for key in sorted(hash) for item in hash[key]]

        
