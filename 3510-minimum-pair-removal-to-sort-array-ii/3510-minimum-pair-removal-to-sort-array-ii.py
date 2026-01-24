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

        temp = [int(x) for x in nums]

        nextIndex = [i + 1 for i in range(n)]
        prevIndex = [i - 1 for i in range(n)]

        alive = [True] * n

        heap = []

        badPairs = 0
        for i in range(n - 1):
            if temp[i] > temp[i + 1]:
                badPairs += 1
            heapq.heappush(heap, (temp[i] + temp[i + 1], i))

        operations = 0

        while badPairs > 0:
            # get valid minimum pair
            while True:
                pair_sum, first = heapq.heappop(heap)
                if alive[first] and nextIndex[first] < n:
                    second = nextIndex[first]
                    if alive[second] and pair_sum == temp[first] + temp[second]:
                        break

            second = nextIndex[first]
            first_left = prevIndex[first]
            second_right = nextIndex[second]

            if temp[first] > temp[second]:
                badPairs -= 1

            if first_left >= 0:
                if temp[first_left] > temp[first] and temp[first_left] <= temp[first] + temp[second]:
                    badPairs -= 1
                elif temp[first_left] <= temp[first] and temp[first_left] > temp[first] + temp[second]:
                    badPairs += 1

            if second_right < n:
                if temp[second_right] >= temp[second] and temp[second_right] < temp[first] + temp[second]:
                    badPairs += 1
                elif temp[second_right] < temp[second] and temp[second_right] >= temp[first] + temp[second]:
                    badPairs -= 1

            if first_left >= 0:
                heapq.heappush(heap, (temp[first_left] + temp[first] + temp[second], first_left))

            if second_right < n:
                heapq.heappush(heap, (temp[first] + temp[second] + temp[second_right], first))
                prevIndex[second_right] = first

            nextIndex[first] = second_right
            temp[first] += temp[second]

            alive[second] = False

            operations += 1

        return operations

        