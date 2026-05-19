class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Solurtion1 dfa
        # n = len(nums)

        # def canReach(index):
        #     if index>=n-1:
        #         return True
        #     return False

        # checked = set()

        # def dfs(index):
        #     if canReach(index):
        #         return True
            
        #     if index in checked:
        #         return False

        #     moves = nums[index]
        #     for jump in range(1,moves+1):
        #         if dfs(index+jump):
        #             return True
        #         checked.add(index+jump)
            
        #     return False


        # return dfs(0)

        #Solution 2 - Greedy
        maxJump = 0 #farthest index reachable given currenmt points explored
        n = len(nums)
        for i in range(n-1):
            if maxJump >= n-1:
                return True
            if maxJump==i and nums[i]==0:
                return False
            maxJump = max(maxJump, i+nums[i])
        return maxJump >= n-1