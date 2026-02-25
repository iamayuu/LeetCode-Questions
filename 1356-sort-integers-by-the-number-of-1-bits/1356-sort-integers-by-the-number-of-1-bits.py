class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        #Solution1 Brute Force
        # ans = []
        # hash = dict()
        # arr.sort()
        # for num in arr:
        #     count = num.bit_count()
        #     if count in hash:
        #         hash[count].append(num)
        #     else:
        #         hash[count]=[num]

        # return [item for key in sorted(hash) for item in hash[key]]

        #Solution2 Optimised
        
        #In Python, when you compare two tuples, it compares them element by element:
        #It looks at the first element (the bit count).
        # If the bit counts are different, that determines the order.
        # If the bit counts are equal, it moves to the second element(the number itself)to break the tie.   
        
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr


        
