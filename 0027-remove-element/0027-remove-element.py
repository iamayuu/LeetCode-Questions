class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        len_nums = len(nums)
        for n in nums[:]:
            if n==val:
                nums.remove(n)
                k=k+1

        return len_nums-k