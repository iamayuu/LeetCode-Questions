class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        #Solution1 (Brute Force) [TLE]
        # ans = 0
        # while sorted(nums) != nums:
        #     min_sum = float("inf")
        #     idx = 1
        #     for i in range(len(nums)-1, 0, -1):
        #         sum = nums[i]+nums[i-1]
        #         if sum <= min_sum:
        #             idx = i
        #             min_sum = sum
        #     nums[idx-1]=nums[idx-1]+nums[idx]
        #     nums.pop(idx)
        #     ans+=1
        # return ans
        
        #Solution2
        n = len(nums)

        nextIndex = [i + 1 for i in range(n)]
        prevIndex = [i - 1 for i in range(n)]
        alive = [True] * n

        heap = []
        badPairs = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                badPairs += 1
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        operations = 0

        while badPairs > 0:
            # extract valid minimum pair
            while True:
                pair_sum, first = heapq.heappop(heap)
                if alive[first] and nextIndex[first] < n:
                    second = nextIndex[first]
                    if alive[second] and pair_sum == nums[first] + nums[second]:
                        break

            second = nextIndex[first]
            left = prevIndex[first]
            right = nextIndex[second]

            if nums[first] > nums[second]:
                badPairs -= 1

            if left >= 0:
                if nums[left] > nums[first] and nums[left] <= nums[first] + nums[second]:
                    badPairs -= 1
                elif nums[left] <= nums[first] and nums[left] > nums[first] + nums[second]:
                    badPairs += 1

            if right < n:
                if nums[right] >= nums[second] and nums[right] < nums[first] + nums[second]:
                    badPairs += 1
                elif nums[right] < nums[second] and nums[right] >= nums[first] + nums[second]:
                    badPairs -= 1

            if left >= 0:
                heapq.heappush(heap, (nums[left] + nums[first] + nums[second], left))

            if right < n:
                heapq.heappush(heap, (nums[first] + nums[second] + nums[right], first))
                prevIndex[right] = first

            nextIndex[first] = right
            nums[first] += nums[second]
            alive[second] = False

            operations += 1

        return operations
