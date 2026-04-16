class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # #Brute Force - TLE
        # n = len(nums)
        # ans = []
        # hmap = dict()
        # for i in range(n):
        #     if nums[i] in hmap:
        #         hmap[nums[i]].append(i)
        #     else:
        #         hmap[nums[i]] = [i]
        # print(hmap)
        # for idx in queries:
        #     res = float("inf")
        #     if len(hmap[nums[idx]]) > 1:
        #         for pos in hmap[nums[idx]]:
        #             if pos != idx :
        #                 res = min(res, abs(idx-pos), n-abs(idx-pos))
        #     else:
        #         res = -1
        #     ans.append(res)
        # return ans

        #Optimized using binary search and nearest logic
        n = len(nums)
        ans = []
        hmap = dict()
        for i in range(n):
            if nums[i] in hmap:
                hmap[nums[i]].append(i)
            else:
                hmap[nums[i]] = [i]
        for idx in queries:
            res = float("inf")
            my_list = hmap[nums[idx]]
            m = len(my_list)
            if m > 1:
                left = 0
                right = m-1
                while left<=right:
                    mid = (left+right)//2
                    if my_list[mid]==idx:
                        break
                    elif my_list[mid]<idx:
                        left=mid+1
                    else:
                        right=mid-1
                pos = my_list[mid-1]
                res = min(res, abs(idx-pos), n-abs(idx-pos))
                pos = my_list[(mid+1)%m]
                res = min(res, abs(idx-pos), n-abs(idx-pos))

            else:
                res = -1
            ans.append(res)
        return ans