class Solution:
    def rotatedDigits(self, n: int) -> int:
        #Brute Force - Working under given constraints
        # hmap = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '9':'6', '8':'8'}
        # def checkGood(num):
        #     temp = ""
        #     snum = str(num)
        #     if '3' in snum or '4' in snum or '7' in snum:
        #         return False

        #     for digit in snum:
        #         temp+=hmap[digit]

        #     return temp!=snum

        # goodNums = 0
        # for i in range(1,n+1):
        #     goodNums+= 1 if checkGood(i) else 0

        # return goodNums

        #Optimal using memorization to use the precomputed results
        # hmap = {0:0, 1:1, 2:5, 5:2, 6:9, 9:6, 8:8}
        # goodNums=0
        # for num in range(1,n+1):
        #     snum = str(num)
        #     if '3' in snum or '4' in snum or '7' in snum:
        #         continue
        #     else:
        #         temp = hmap[num//10]*10+hmap[num%10]
        #         hmap[num]=temp
        #         if temp!=num:
        #             goodNums+=1
        # return goodNums

        #Solution 3
        res = 0
        for num in range(1, n + 1):
            curr = str(num)
            if "3" in curr or "4" in curr or "7" in curr:
                continue
            if "2" in curr or "5" in curr or "9" in curr or "6" in curr:
                res += 1
        return res