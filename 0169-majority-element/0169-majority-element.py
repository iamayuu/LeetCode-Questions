from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Solution 1 (using counter most common)
        # count = Counter(nums)
        # return count.most_common(1)[0][0]

        #Solution 2 (using counter and finding value with >n/2)
        count = Counter(nums)
        for i in count:
            if count[i]>len(nums)/2:
                return i