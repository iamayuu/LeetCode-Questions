class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # #Brute FORCE
        # hmap = dict()
        # for i,num in enumerate(nums):
        #     if num in hmap:
        #         hmap[num].append(i)
        #     else:
        #         hmap[num]=[i]
        
        # arr = []
        # for i,num in enumerate(nums):
        #     mylist = hmap[num]
        #     if len(mylist)>1:
        #         sum=0
        #         for idx in mylist:
        #             sum+=abs(i-idx)
        #         arr.append(sum)
        #     else:
        #         arr.append(0)
        
        # return arr

        #Prefix Sum
        n = len(nums)
        count_right = dict()
        count_left = dict()
        lastseen_right = dict()
        lastseen_left = dict()
        prefixsum_right = [0]*n
        prefixsum_left = [0]*n
        for i in range(n):
            #Right part i.e. processing left to right
            num=nums[i]
            if num in lastseen_right:
                lastseen_idx = lastseen_right[num]
                prefixsum_right[i] = prefixsum_right[lastseen_idx]+lastseen_right[num]
            lastseen_right[num]=i

            #Left part i.e. processing right to left
            i=n-1-i
            num=nums[i]
            if num in lastseen_left:
                lastseen_idx = lastseen_left[num]
                prefixsum_left[i] = prefixsum_left[lastseen_idx]+lastseen_left[num]
            lastseen_left[num]=i

        arr = [0]*n
        for i in range(n):
            #calculating and adding for right part
            num = nums[i]
            if num in count_right:
                arr[i] += (i*count_right[num])-prefixsum_right[i]
                count_right[num]+=1
            
            else:
                count_right[num]=1
            #calculating and adding for left part
            i=n-1-i
            num = nums[i]
            if num in count_left:
                arr[i] += prefixsum_left[i]-(i*count_left[num])
                count_left[num]+=1
            
            else:
                count_left[num]=1
        
        return arr